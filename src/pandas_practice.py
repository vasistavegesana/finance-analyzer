import pandas as pd

df = pd.read_csv("data/expenses.csv")

df.dropna(inplace = True)

df["amount"] = df["amount"].astype(float)

total = df.groupby("category")["amount"].sum()
print(total)
print(df.info())