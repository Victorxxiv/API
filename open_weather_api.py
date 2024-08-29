import requests

# API key from OpenWeather
API_KEY = '76b624388d75ae734318a1cb25064beb'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


# City name
def get_weather(city_name):
    # API URL
    params = {
        'q': city_name,  # 'q' query parameter for city name
        'appid': API_KEY,  # 'appid' query parameter for API key
        'units': 'metric'  # For temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return weather
    else:
        return {'error': f"City {city_name} not found."}


if __name__ == '__main__':
    city = input("Enter city name: ")
    weather_info = get_weather(city)
    print(weather_info)
