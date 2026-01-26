# L27. Lego! - Manipulating Data
print("Task 1: Understanding the Dataset")
print("Task 2: Reviewing Data Quality")
print("Task 3: Data Visualisation")
print("Task 4: Independent Analysis")

c = input("Enter a task to view (1-4): ")

if c == "1":
    import pandas as pd
    df = pd.read_csv('lego_sets.csv')
    print(df.head())
    print(df.tail())
    print(df.info())

elif c == "2":
    import pandas as pd
    df = pd.read_csv('lego_sets.csv')
    print(df.isnull())
    print(df.info())
    print(df.describe())

elif c == "3":
    print("1. Histrogram of Lego prices")
    print("2. Scatter plot: Piece count vs Price")
    print("3. Bar Chart: Top 10 Lego themes by rating")
    c2 = input("Enter a choice to view one of the 3 graphs (1-3): ")
    
    if c2 == "1":
        import matplotlib.pyplot as plt
        import pandas as pd
        df = pd.read_csv('lego_sets.csv', header = None ,quoting=2)
        df.hist()
        plt.xlim([0,])
        plt.ylim([50,500])
        plt.title("Histrogram of LEGO prices")
        plt.xlabel("")
        plt.ylabel("")
        plt.show()
        # UNFINISHED TASK 3



elif c == "4":
    print("1. Top 5 Most Expensive Sets")
    print("2. Average price by theme")
    c3 = input("Enter a choice between these 2 to view(1-2): ")
    if c3 == "1":
        import pandas as pd
        df = pd.read_csv('lego_sets.csv')
        print(df['list_price'].nlargest(n=5))
    else:
        import pandas as pd
        df = pd.read_csv('lego_sets.csv')
        column_averages = df["theme_name"].mean()
        print(column_averages)