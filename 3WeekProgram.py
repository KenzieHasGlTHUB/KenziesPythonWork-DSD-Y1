import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def load_data():
    try:
        data = pd.read_csv("GameShop.csv")
        print("Dataset loaded successfully")
        return data
    except FileNotFoundError:
        print("Error: GameShop.csv file not found.")
        return None



def calculate_statistics(data):
    try:
        revenue = data["Total Revenue (£)"]

        stats = {
            "Total Revenue": np.sum(revenue),
            "Average Revenue": np.mean(revenue),
            "Max Revenue": np.max(revenue),
            "Min Revenue": np.min(revenue)
        }

        return stats

    except Exception as e:
        print("Error calculating statistics:", e)


def bar_chart_category(data):
    try:
        category_sales = data.groupby("Category")["Total Revenue (£)"].sum()

        category_sales.plot(kind="bar")
        plt.title("Revenue by Game Category")
        plt.xlabel("Category")
        plt.ylabel("Revenue (£)")
        plt.show()

    except Exception as e:
        print("Error creating bar chart:", e)



def line_chart_sales(data):
    try:
        daily_sales = data.groupby("Date")["Total Revenue (£)"].sum()

        daily_sales.plot(kind="line", marker="o")
        plt.title("Daily Revenue Trend")
        plt.xlabel("Date")
        plt.ylabel("Revenue (£)")
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        print("Error creating line chart:", e)



def pie_chart_units(data):
    try:
        units = data.groupby("Category")["Units Sold"].sum()

        units.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Units Sold by Category")
        plt.ylabel("")
        plt.show()

    except Exception as e:
        print("Error creating pie chart:", e)



def main():
    data = load_data()

    if data is not None:

        stats = calculate_statistics(data)

        print("\nGame Shop Statistics")
        for key, value in stats.items():
            print(key, ":", round(value, 2))

        bar_chart_category(data)
        line_chart_sales(data)
        pie_chart_units(data)



if __name__ == "__main__":
    main()