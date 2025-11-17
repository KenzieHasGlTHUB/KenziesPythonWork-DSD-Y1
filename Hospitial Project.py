# Hospitial Project

name=input("Enter Patients Name: ")
age=int(input("Enter the Patients Age: "))
bill=float(input("Please enter the bill amount: "))

if age < 18:
    bill / 0.20
else:
    print()
if bill > 1000:
    question=input("Your bill is incredibly high, So, would you rather do monthly payments of 100 for the next 10 months? Yes/No: ")
    if question== "no":
        print("Ok, that is your option, Here are your final formatted details and bill price: ")
    else:
        print()
print("Your details are:", name, age, "And your total bill cost is", bill)
questiontwo=input("Am i correct? ")
if questiontwo == "yes":
    print("Thank you.")
else:
    print("Please restart the program and do it again.")