# Task 3: Score Logger

print("Welcome to the score logger menu")
print("1. Enter new name and score: ")
print("2. View previous scores: ")

option=input("Enter an option: ")

if option == "1":
    name = input("Enter your name: ")
    score = input("Enter your score: ")
    with open("score.txt", "a") as file:
        file.write(f"{name}: {score}\n")
        print("Score saved to score.txt!")
    
    
   
