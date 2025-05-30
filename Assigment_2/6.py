to_conduct = float(input("Введіть число для перевірки на знак: "))

if to_conduct > 0:
    print("Позитивний")
elif to_conduct < 0:
    print ("Негативний")
else:
    print("Нуль")