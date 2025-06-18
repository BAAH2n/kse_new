import requests
import pandas as pd

def get_coordinates(city, api_key):
    response = requests.get('https://api.api-ninjas.com/v1/geocoding?city={}'.format(city), headers={'X-Api-Key': api_key})
    coordinates = response.json()
    city_latitude = coordinates[0]["latitude"]
    city_longitude = coordinates[0]["longitude"]
    data = [city_latitude, city_longitude]
    return data

def get_7days_forecast(latitude, longitude):
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}38&hourly=temperature_2m,wind_speed_10m')
    d = response.json()["hourly"]
    df = pd.DataFrame(data=d)
    #print(df.to_string(index=False))
    return df