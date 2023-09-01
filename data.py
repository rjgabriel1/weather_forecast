import os
import requests
from dotenv import load_dotenv

API_KEY = os.getenv('API_KEY')


def get_weather_data(city, days_count=None, kind=None):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}'

    response = requests.get(url)
    data = response.json()
    # Filter data by number of days and kind
    filtered_data = data['list']
    nr_values = 8*days_count
    filtered_data = filtered_data[:nr_values]
    match kind:
        case 'Temperature':
            filtered_data = [result['main']['temp']
                             for result in filtered_data]
        case 'Sky':
            filtered_data = [result['weather'][0]['main']
                             for result in filtered_data]

    return filtered_data


if __name__ == '__main__':
    print(get_weather_data('lisbon', 2, 'Sky'))
