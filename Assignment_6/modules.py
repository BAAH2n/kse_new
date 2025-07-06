import requests as r
from datetime import datetime, timedelta
import pandas as pd

def get_info (crypto, time_period):
    params = {
    'vs_currency': 'usd',
    'days': time_period,
    'interval': 'daily'
    }
    response = r.get(f'https://api.coingecko.com/api/v3/coins/{crypto}/market_chart', params=params)
    data = response.json()
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('date', inplace=True)
    df.drop('timestamp', axis=1, inplace=True)
    return df
