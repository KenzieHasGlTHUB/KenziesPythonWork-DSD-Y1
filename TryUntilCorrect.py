# Menu System Password checker.
def passwordchecker():
    counter = 1
    password=("123ABC")
    password=input("Please Enter Your Password: ")
    while True:
        counter = counter + 1
        if password != "123ABC":
            print("Wrong! Try Again.")
            password=input("Please enter your password:")
            counter = int(counter)
            if counter == 3:
                print("Locked out.")
                break
        elif password == "123ABC":
            print("Password Correct!")
passwordchecker()
    