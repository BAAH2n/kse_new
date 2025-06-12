import pandas as pd
import numpy as np

df = pd.read_csv("transactions.csv")
task1 = df[df["product_type"] == "groceries"]
task2 = df['amount'].max()

df2 = df[df['amount'] == task2]
transaction_date = df2['transaction_date']
sum_amount = sum(df['amount'])
df["Відсоток від суми"] = df['amount']*100/sum_amount
print(transaction_date)
print(sum_amount)
print(df.shape)
df3 = df.groupby('country')['shipping_cost'].mean()
print(df3.sort_values(ascending=False))
df['country'] = np.where(df['country'] is None, "Not definded county")
