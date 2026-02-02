# PixelVault Data Analysis

print("Task 1: Load and Inspect the Dataset")
print("TASK 2 DIDNT NEED ANY CODING")
print("Task 3: Data Quality Checks")
print("Task 4: Inital Insights")
print("TASK 5 DIDNT NEED ANY CODING")


choice=input("Enter what task to view: ")


if choice == "1" :
    import pandas as pd
    df = pd.read_csv("pixelvault game sales.csv")
    print(df.head)
    print(df.tail)
    print(df.describe)
    print(df.info)

elif choice == "3":
    import pandas as pd
    df = pd.read_csv("pixelvault game sales.csv")
    print(df.isnull())
    print(df.duplicated())


else:
    import pandas as pd
    df = pd.read_csv("pixelvault game sales.csv")
    frequent_game = df["game_title"].value_counts()
    category = df["category"].value_counts()
    print(df.describe())
    print(frequent_game)
    print(category)
