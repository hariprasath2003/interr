import pandas as pd
import requests


def fetch_weather_data(api_key, cities):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    weather_data = []

    for city in cities:
        params = {'q': city, 'appid': api_key, 'units': 'metric'}
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 600:
            city_data = {
                'City': city,
                'Temperature (Celsius)': data['main']['temp'],
                'Humidity (%)': data['main']['humidity'],
                'Weather Description': data['weather'][0]['description'],
            }

            weather_data.append(city_data)
        else:
            print(f"Error fetching data for {city}: {data.get('message', 'Unknown error')}")

    return weather_data


def save_to_csv(data, filename='weather_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")


if __name__ == "__main__":
    
    api_key = 'YOUR_API_KEY'
    cities = ['London', 'New York', 'Tokyo', 'Paris', 'Sydney']

    weather_data = fetch_weather_data(api_key, cities)
    save_to_csv(weather_data)
