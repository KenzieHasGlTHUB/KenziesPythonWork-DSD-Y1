# Select a task to test run:
print("What task would you like to run?")
print("Task 1: Creating Lists")
print("Task 2: Indexing Challenge")
Task = input("Enter what task you'd like to run 1-2: ")

# Task 1: Creating Lists
if Task == "1":
    print("A: Energy Levels")
    print("B: Wellbeing app usernames")
    print("C: Step-count values from the past week")
    select=input("What list would you like to enter to?: ")
    if select == "A":
        fiveenergylevels = ["Diet", "Meals", "Exercise", "Sleep Schedule", "Don't oversleep",]
        print(fiveenergylevels)
        print("Here are the 3 important energy levels: ")
        print(fiveenergylevels [0])
        print(fiveenergylevels [2])
        print(fiveenergylevels [4])
        q1 = input("Would you like to add something to this list? (Y/N): ")
        if q1 == "Y":
            One = input("Enter a new energy level that you do throughout the day: ")
            fiveenergylevels.append(One)
            print(fiveenergylevels)
        else:
            print()
    elif select == "B":
        print("Here are some usernames from a wellbeing app: ")
        usernames = ["WellbeingWarrior", "MindfulMoments", "ZenZone", "Happythoughts", "InnerPeaceQuest",]
        print(usernames)
        q2 = input("Would you like to add something to this list? (Y/N): ")
        if q2 == "Y":
            two = input("Enter a new user to this list: ")
            usernames.append(two)
            print(usernames)
# Task 1 UNFINSHED

#Task 2: Indexing Challenge
elif Task == "2":
    screen_times = [120, 95, 140, 160, 80, 100, 200]
    print("Day 3 screentime: ", screen_times[2])
    average = screen_times[0] + screen_times[1], + screen_times[2]
    print("Average of day 1-3: ", average)
    replace = int(input("Replace the last value: "))
    screen_times.pop[replace, -1]
    print(max(screen_times))
    print(min(screen_times))
# Task 2: Finished

# Task 3: List Compare Mini-Investigation

elif Task == "3":
    listA = [1,2,3]
    listB = [1, "2", 3.0]
# got confused at this

#Task 4: Digital Wellbeing Analysis
elif Task == "4":
    notifs = [34, 28, 55, 40, 60, 22, 18]
    print("The highest day is: ", notifs[2])
    print("The lowest day is:", notifs[6])
    total_notifs = notifs[0], + notifs[1], + notifs[2], + notifs[3], + notifs[4], + notifs[5], + notifs[6]
    print("The total notifications are: ", total_notifs)
    average_notifs = total_notifs / 7
    print("The average amount of notifs per day is: ", average_notifs)
