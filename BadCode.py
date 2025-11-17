def hospital():
    Name=input("enter Patient Name:")
    Age = int(input("AGE:"))
    height= input("height")
    weight= input("WEIGHT")
    bmi= float(weight)/(float(height)*float(height))
    if bmi > 30:
        print("overweight")
    else:
        print("ok")
    if Age >= 65:
        print("Old person discount applied")
    print("Patient:",Name,"has bmi of",bmi)
hospital()