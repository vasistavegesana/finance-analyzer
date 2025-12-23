import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/expenses.csv")

df.dropna(inplace = True)

df["amount"] = df["amount"].astype(float)

category_total = df.groupby("category")["amount"].sum()

category_total.plot(kind = "bar")
plt.title("Total Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Total Spent")

sns.barplot(x = category_total.index, y = category_total.values, palette = "viridis")
plt.show()