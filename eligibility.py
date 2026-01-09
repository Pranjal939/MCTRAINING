def eligiblity_checker(): 
    print("welcome to eligibility checker:")
for i in range(1,11):
    age = int(input(f"enter your age :"))
    marks = float(input(f"enter ypur marks :"))
    state = input(f"enter the state (GJ for gujarat , DL for delhi, O for others ) :")
    if age <= 20 and marks >= 60:
        print("you are eligible for apply !")
    elif age <= 20 and marks >=50 and state == 'GJ':
        print("you are eligible for apply !")
    elif age <= 22 and marks >=60 and state == "DL":
        print("you are eligible for apply !")
    else :
        print("ypu are not eligible to apply !")
    choice = input("do you want to check another eligibility :")
    if choice.upper() != 'Y':
        break
    print("thank you for using Eligibility chcker !")