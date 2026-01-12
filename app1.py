import streamlit as st
import sqlite3
import datetime

# ---------- Database Connection ----------
def con():
    c = sqlite3.connect('fittrack.db', check_same_thread=False)
    cr = c.cursor()

    cr.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT
        )
    ''')

    cr.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            wid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            date TEXT,
            exercise TEXT,
            duration INTEGER,
            calories_burned INTEGER,
            FOREIGN KEY(userid) REFERENCES users(id)
        )
    ''')

    return c, cr

c, cr = con()

# ---------- UI ----------
st.title("🏋️ Fit Track App")

menu = st.sidebar.selectbox(
    "Menu",
    ["Register User", "Log Exercise", "View User Workouts", "View All Users"]
)

# ---------- Register User ----------
if menu == "Register User":
    st.header("Register User")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    if st.button("Register"):
        cr.execute(
            "INSERT INTO users(name, age, gender) VALUES (?, ?, ?)",
            (name, age, gender)
        )
        c.commit()

        uid = cr.execute(
            "SELECT id FROM users WHERE name = ?",
            (name,)
        ).fetchone()[0]

        st.success(f"User {name} registered successfully with ID {uid}")

# ---------- Log Exercise ----------
elif menu == "Log Exercise":
    st.header("Log Exercise")

    uid = st.number_input("User ID", min_value=1)
    exercise = st.text_input("Exercise Name")
    duration = st.number_input("Duration (minutes)", min_value=1)
    calories = st.number_input("Calories Burned", min_value=1)

    if st.button("Log Exercise"):
        date = datetime.date.today().strftime('%Y-%m-%d')

        user = cr.execute(
            "SELECT id FROM users WHERE id = ?",
            (uid,)
        ).fetchone()

        if user:
            cr.execute(
                '''INSERT INTO workouts(userid, date, exercise, duration, calories_burned)
                   VALUES (?, ?, ?, ?, ?)''',
                (uid, date, exercise, duration, calories)
            )
            c.commit()
            st.success("Exercise logged successfully")
        else:
            st.error("User ID not found")

# ---------- View User Workouts ----------
elif menu == "View User Workouts":
    st.header("User Workouts")

    uid = st.number_input("Enter User ID", min_value=1)

    if st.button("View Workouts"):
        rs = cr.execute(
            "SELECT date, exercise, duration, calories_burned FROM workouts WHERE userid = ?",
            (uid,)
        ).fetchall()

        if rs:
            st.table(rs)
        else:
            st.info("No workouts found")

# ---------- View All Users ----------
elif menu == "View All Users":
    st.header("All Users")

    rs = cr.execute("SELECT * FROM users").fetchall()
    st.table(rs)