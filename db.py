import sqlite3
import datetime

def con():
    c=sqlite3.connect('fittrack.db')
    cr=c.cursor()
    q1='''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,gender TEXT)'''
    cr.execute(q1)

    q2='''CREATE TABLE IF NOT EXISTS Workouts(wid INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER, date TEXT, exercise TEXT, duration INTEGER, calories_burned INTEGER,
        FOREIGN KEY(userid) REFERENCES users(id))'''

    cr.execute(q2)
    return c

def main():
    c=con()
    print("welcome to fit track")
    print('Main menu')
    print('1. Register User')
    print('2. Log Exercise')
    print('3. add exerices')
    print('4. view all users')
    print('5.Exit')
    choice=input('Enter Your Choice: ')
    if choice=='1':
        cr = c.cursor()
        n=input('Enter Name:')
        a=int(input('Enter Age:'))
        g=input('Enter Gender:')
        cr=c.cursor()
        q='INSERT INTO users(name,age,gender) VALUES(?,?,?)'
        cr.execute(q,(n,a,g))
        c.commit()
        q2='SELECT id FROM users WHERE name=?'
        rs=cr.execute(q2,(n,)).fetchall()
        id=rs[0][0]
        print(f'user {n} register successfull with id',id)

    elif choice == '2':
        cr= c.cursor()
        uid = int(input("enter user id"))
        date = datetime.date.today().strftime('%Y-%m-%d')
        exercise = input("enter exercise name :")
        duration = int(input("enter duration (in minutes):"))
        calories_burned = int(input("enter calories burned"))
        q = 'INSERT INTO Workouts (userid, date, exercise, duration, calories_burned) VALUES (?,?,?,?,?)'
        cr.execute(q,(uid,date,exercise,duration,calories_burned))
        c.commit()
        print('enter logged successfully')

    elif choice=='3':
        cr=c.cursor()
        uid = int(input('enter user id'))
        q = 'SELECT * FROM Workouts WHERE userid=?'

    elif choice=='4':
        cr=c.cursor()
        q='SELECT* FROM users'
        rs=cr.execute(q).fetchall()
        for row in rs:
            print(f'ID: {row[0]}, Name: {row[1]}, Age: {row[2]}')

    elif choice=='5':
        print('exiting ')

    c.close()

if __name__=="__main__":
    main()