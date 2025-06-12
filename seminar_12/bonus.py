import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("transactions.csv")
sum_amount = sum(df['amount'])
series = df['payment_method'].value_counts()
combined = df.groupby('payment_method')['amount'].sum()
end = pd.DataFrame(combined)
end['amount'] = end['amount']/sum_amount
end['amount'].plot.pie(autopct='%1.1f%%')

plt.title('Продажі за категоріями')
plt.ylabel('')  
plt.show()