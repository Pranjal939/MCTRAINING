#print('this is deom spython script')
#import numpy as np
#print('numpy version:',np.__version__)pranjal
#import sklearn
#print(sklearn.__version__)
#import numpy
#virctual environment 
#python ~m venv en #type in terminal 
#username = input("enter username:")
#marks = float(input("enter marks:"))
#print(f'welcome {username},marks :%5.4d' %marks)

#s1 = 'GeeksforGeeks'
#s2 = ' 2nd line'
#print(s1[::-1],end='@')
#print(end = '@')
#list = s2.split()
#s3 = "".join([i.capitalize() for i in list])
#print(s3)

#lst = [1,10,'abc',5,6]
#print(lst)
#print(lst.pop())

#products = {'laptop' :800,'mouse':200}
#print(products.update({'monitor' : 1000}))
#print(products)
#create a program to cofify or not  g=110

def check_qualification(state, subject, marks, total_score):
    percentage = (marks / total_score) * 100
    
    if state.lower() == "gujarat":
        if percentage >= 50:
            return True
        else:
            return False
    else:
        if percentage >= 60:
            return True
        else:
            return False
name = input("Enter student name: ")
state = input("Enter student state: ")
subject = input("Enter subject: ")
marks = float(input("Enter marks obtained: "))
total_score = float(input("Enter total marks: "))

if check_qualification(state, subject, marks, total_score):
    print(f"{name} from {state} is qualified for the entrance exam in {subject}.")
else:
    print(f"{name} from {state} is NOT qualified for the entrance exam in {subject}.")


