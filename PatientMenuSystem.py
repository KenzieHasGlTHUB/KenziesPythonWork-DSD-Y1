# Task 6 Patient Menu System.
def patientmenusystem():
    print("1. Patient Details")
    print("2. BMI Calculator")
    print("3. Medicine Dosage")
    print("4. Exit the menu")
    choice=input("Where would u like to go?: ")
    
    if choice == "1":
       name=input("Please enter the patients name: ")
       age=input("Please enter the patients age: ")
       print("These are your patient details, Correct?",age, name)

    elif choice == "2":
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
    
    elif choice == "3":
       medicine_dosage=input("Please enter how much medicine are u taking per day (tablets): ")
       maximum_dosage= 4
       if medicine_dosage > maximum_dosage: 
          print(f"WARNING: Total dosage exceeds the safe limit of {maximum_dosage} mg!")
        elif medicine_dosage < 4:
          print("Warning, Your taking less tablets then usual, Please make sure you are taking the maximum dosage per day")
          else:
          print("Well done your taking the maximum dosage you should be per day.")
    else:
       print("Exiting...")
    break
patientmenusystem()