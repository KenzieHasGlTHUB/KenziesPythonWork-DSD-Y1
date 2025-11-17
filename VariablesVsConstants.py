
# Scenario 1: Patient Record System

#print("Welcome to your digital record, Please enter down your details asked below: ")
#name=input("Please, enter your name: ")
#age=int(input("Enter your age: "))
#height=float(input("Enter your height: "))
#print("So your details are: ", name, age, height)
#question=input("Am i correct? y/n: ")
#if question=="Y" or "y" or "yes":
#    print("Thank you, your digital record won't take a while.")
#else:
#    print("Please run this again and correct the details."

# Scenario 2: BMI Calculator

#weight=int(input("Enter your weight (KG): "))
#height=float(input("Enter your height (in meters): "))
#height * 2
#BMI = weight / height
#if BMI >= 18.49:
#    print("You are underweight. Having a BMI of: ", BMI)
#elif BMI <= 18.5:
#    print("You have healty weight, Having a BMI of: ", BMI)
#elif BMI <= 25: 
#    print("You are overweight... Having a BMI of: ", BMI)
#else:
#    print("You are obese, Having a BMI of: ", BMI)

# Scenario 3: Medicine Dosage Trackingm

#medicine_dosage=input("Please enter how much medicine are u taking per day (tablets): ")
#maximum_dosage= 4
#
# if medicine_dosage > maximum_dosage: 
#            print(f"WARNING: Total dosage exceeds the safe limit of {maximum_dosage} mg!")
#
 #   elif medicine_dosage < 4:
  #    print("Warning, Your taking less tablets then usual, Please make sure you are taking the maximum dosage per day")
#
 #   else:
  #    print("Well done your taking the maximum dosage you should be per day.")


# Scenario 4: Hospitial Billing System

#total_cost = 0
#rooms= 10
#number_of_days= 0
#medical_treatment = 20
#print("I will be asking you a couple of questions and please answer them so we can know how much you will be charging.")
#rooms_cost=input("Did you pay for a room?: ")
#if "yes":
#    total_cost + rooms
#else:
#    total_cost= 0
#days=int(input("How many days have u stayed?: "))
#days * total_cost
#treatment=input("Were you given any medical treatment?: ")
#if "yes":
#    total_cost + medical_treatment
#else:
#    total_cost + 0
#VAT = 1.2
#total_cost * VAT
#print("Your VAT/Total cost is:", total_cost)


# FINAL TASK

def digital_record

print("Welcome to your digital record, Please enter down your details asked below: ")
name=input("Please, enter your name: ")
age=int(input("Enter your age: "))

height=float(input("Enter your height: "))
weight=int(input("Enter your weight (KG): "))
height=float(input("Enter your height (in meters): "))
height * 2
BMI = weight / height

if BMI >= 18.49:
    print("You are underweight. Having a BMI of: ", BMI)
elif BMI <= 18.5:
    print("You have healty weight, Having a BMI of: ", BMI)
elif BMI <= 25: 
    print("You are overweight... Having a BMI of: ", BMI)
else:
    print("You are obese, Having a BMI of: ", BMI)
print("So your details are: ", name, age, height, BMI)
question=input("Am i correct? y/n: ")
if question=="Y" or "y" or "yes":
    print("Thank you, your digital record won't take a while.")
else:
    print("Please run this again and correct the details.")

question=input("Have u needed any medicine recently?: ")
if question="yes":
     medicine_dosage=input("Please enter how much medicine are u taking per day (tablets): ")
     maximum_dosage= 4
     if medicine_dosage > maximum_dosage: 
           print(f"WARNING: Total dosage exceeds the safe limit of {maximum_dosage} mg!")
    elif medicine_dosage < 4:
     print("Warning, Your taking less tablets then usual, Please make sure you are taking the maximum dosage per day")
    else:
     print("Well done your taking the maximum dosage you should be per day.")
else:
total_cost = 0
rooms= 10
number_of_days= 0
medical_treatment = 20
print("I will be asking you a couple of questions and please answer them so we can know how much you will be charging.")
rooms_cost=input("Did you pay for a room?: ")
if "yes":
    total_cost + rooms
else:
    total_cost= 0
days=int(input("How many days have u stayed?: "))
days * total_cost
treatment=input("Were you given any medical treatment?: ")
if "yes":
    total_cost + medical_treatment
else:
    total_cost + 0
VAT = 1.2
total_cost * VAT
print("Your VAT/Total cost is:", total_cost)

