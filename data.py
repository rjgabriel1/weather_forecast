import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_weather_data(city, days_count=None,):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'

    response = requests.get(url)
    data = response.json()
    # Filter data by number of days
    filtered_data = data['list']
    nr_values = 8*days_count
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == '__main__':
    print(get_weather_data('lisbon', 2))
