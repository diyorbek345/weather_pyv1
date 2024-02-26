import requests
from config import open_weather_token

def get_weather(city,open_weather_token = open_weather_token):
    try:
        responce = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
        data = responce.json()
        # print(data)
        city_name = data['name']
        cur_temperature = data['main']['temp']
        cur_humidity = data['main']['humidity']

        return f'Shahar nomi: {city_name}\nTemperatura: {cur_temperature}\nNamlik: {cur_humidity}'


    except Exception as Ex:
        print(Ex)
        print("Shahar nomini tekshiring")

def main():
    city = input("Shahar nomini kiriting:\n")
    print(get_weather(city=city))

if __name__ == '__main__':
    main()