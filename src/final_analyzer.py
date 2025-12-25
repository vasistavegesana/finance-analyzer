import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constant Variables
monthly_income = 7500
path = "data/expenses.csv"

#Function to read the expenses file
def file_reader(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to clean the data from the dataframe
#   - Drops any rows with missing values
#   - Converts the "amount" column to float type so that 
#     mathematical operations can be performed on it as 
#     it is stored as string by default
def clean_df(df):
    df.dropna(inplace=True)
    df["amount"] = df["amount"].astype(float)
    return df

# Function to analyze expense data from the dataframe
#   - Groups expenses by category
#   - Calculates total spending per category
#   - Calculates overall total expenses across all categories
#   - Identifies the category with the highest spending
#   - Identifies the category with the lowest spending
#   - Returns all computed results in a dictionary so they can be
#     reused by other functions (printing insights and plotting)
def analyze_expenses(df):
    category_totals = df.groupby("category")["amount"].sum()
    total_expenses = category_totals.sum()

    highest_category = category_totals.idxmax()
    highest_amount = category_totals.max()

    lowest_category = category_totals.idxmin()
    lowest_amount = category_totals.min()

    return {
        "category_totals": category_totals,
        "total_expenses": total_expenses,
        "highest_category": highest_category,
        "highest_amount": highest_amount,
        "lowest_category": lowest_category,
        "lowest_amount": lowest_amount,
    }

# Function to print financial insights in a human-readable format
#   - Calculates remaining money after expenses
#   - Displays total expenses and remaining balance
#   - Shows the category with the highest spending and its amount
#   - Shows the category with the lowest spending and its amount
#   - Uses values already computed in the analysis dictionary
def print_analysis(analysis, income):
    remaining_money = income - analysis["total_expenses"]

    print("\n📊 FINANCIAL INSIGHTS")
    print("-" * 30)
    print("Total Expenses:", analysis["total_expenses"])
    print("Remaining Money:", remaining_money)
    print(
        "Highest Spending Category:",
        analysis["highest_category"],
        f"(${analysis['highest_amount']})",
    )
    print(
        "Lowest Spending Category:",
        analysis["lowest_category"],
        f"(${analysis['lowest_amount']})",
    )

# Function to visualize expense data by category
#   - Uses Seaborn to create a clean and styled bar chart
#   - Uses Matplotlib to control figure size, titles, labels,
#     and layout
#   - Displays total expenses grouped by category for easy
#     comparison
#   - Helps identify which categories have the highest and 
#     lowest spending
def plot_expenses(category_totals):

    plt.figure(figsize = (10,6))

    sns.barplot(
        x = category_totals.index,
        y = category_totals.values,
        palette = "viridis"
    )

    plt.title("Total Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Spent")

    plt.tight_layout()

    plt.show()

   
def main():
    df = file_reader(path)
    df = clean_df(df)
    analysis = analyze_expenses(df)
    print_analysis(analysis, monthly_income)
    plot_expenses(analysis["category_totals"])