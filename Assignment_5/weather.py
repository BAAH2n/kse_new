import modules as m

#city = input('Введіть назву вашого міста: ')
city = "Kyiv"
api_key_ninja = '272d0hkKBLhjV0UHXQ0KkA==qkVfsUZA3foqwmoI'

coordinates = m.get_coordinates(city, api_key_ninja)
latitude = coordinates[0]
longitude = coordinates[1]

df = m.get_7days_forecast(latitude, longitude)
first_3_days = df.head(72)

print(f"""Максимальна температура за наступні 3 дні: {first_3_days["temperature_2m"].max()}
Мінімальна: {first_3_days["temperature_2m"].min()}
Середня: {first_3_days["temperature_2m"].mean()}""")

n = 0
for i in df["wind_speed_10m"]:
    if i > df["wind_speed_10m"].mean():
        n += 1

print(f"{n} годин швидкість вітру була більша за середню")
