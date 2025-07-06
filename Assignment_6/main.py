import modules 

in_position = False
quantity = 0

crypto = input("Введіть назву монетки маленькими буквами: ")
time_period = str(input("За яку к-сть минулих днів ви хочете бачити сигнали? (більше 30) "))
position = float(input("Яка сума у вас є для торгівлі? "))

wallet = position

df = modules.get_info(crypto, time_period)
df['SMA5'] = df['price'].rolling(window=5).mean()
df['SMA30'] = df['price'].rolling(window=30).mean()

df['Signal'] = 0
df.loc[df['SMA5'] > df['SMA30'], 'Signal'] = 1
df.loc[df['SMA5'] < df['SMA30'], 'Signal'] = -1

for date, row in df.iterrows():
    price = row['price']
    signal = row['Signal']
    if signal == 1 and not in_position:
        quantity = wallet / price
        wallet -= quantity * price
        in_position = True
    elif signal == -1 and in_position:
        wallet += quantity * price
        quantity = 0
        in_position = False

if in_position:
    last_price = df['price'].iloc[-1]
    wallet += quantity * last_price
    quantity = 0
    in_position = False

print(f"Загальний прибуток стратегії: {wallet-position} USD")

print (df)