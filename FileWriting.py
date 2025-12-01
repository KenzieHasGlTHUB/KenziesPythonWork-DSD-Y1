print("This is the work i've done with Lesson 20, Working with Files:")
print("1. Random Number Generator")
print("2. ScoreLogger (NOT FINISHED)")
option=input("Pick one of these to test.")
if option == "1":
    import random
    with open("scores.txt", "a") as file:
        for i in range(100):
            randomlist = random.randint(1, 100)
    file.write(str(randomlist) + '\n')
elif option == "2":
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
    
    