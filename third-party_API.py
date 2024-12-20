import requests
from datetime import datetime

from config_data.bot_config import API_KEY


class CityWeather:

    def __init__(self, city_name: str) -> None:
        self.__city_name = city_name
        self.__api_id = API_KEY

    def __get_id(self) -> int:
        """
        Получение ID города

        :return: city_id
        """

        options: dict[str, str | int] = {
            'q': self.__city_name,
            'type': 'like',
            'units': 'metric',
            'APPID': self.__api_id
        }

        try:
            common_response: requests = requests.get('http://api.openweathermap.org/data/2.5/find', params=options)
            common_data: dict[str, any] = common_response.json()
            city_id: int = common_data['list'][0]['id']

        except Exception: # noqa E722
            city_id = 0

        return city_id

    def get_weather(self) -> dict[str, str]:
        """
        Получение погоды по ID города

        :return: result_data
        """
        date_time: str = datetime.now().strftime('%d.%m.%Y в %H:%M:%S')

        options: dict[str, str | int] = {
            'id': self.__get_id(),
            'units': 'metric',
            'lang': 'ru',
            'APPID': self.__api_id
        }

        if self.__get_id != 0:
            weather_response: requests = requests.get("http://api.openweathermap.org/data/2.5/weather", params=options)
            weather_data: dict[str, str | int] = weather_response.json()

            result_data: dict[str, str] = {
                'date': date_time,
                'name': weather_data['name'],
                'desc': weather_data['weather'][0]['description'], # noqa Type error
                'temp': str(weather_data['main']['temp']), # noqa Type error
                'feel': str(weather_data['main']['feels_like']), # noqa Type error
                'wind': str(weather_data['wind']['speed']), # noqa Type error
                'humid': str(weather_data['main']['humidity']), # noqa Type error
                'press': str(weather_data['main']['pressure']), # noqa Type error
                'vis': str(weather_data['visibility'] / 1000)
            }

        else:
            result_data: dict[str, str] = {
                'name': self.__city_name[:-3],
                'date': date_time,
                'desc': 'Данные о погоде не найдены',
                'temp': 'Данные о погоде не найдены',
                'feel': 'Данные о погоде не найдены',
                'wind': 'Данные о погоде не найдены',
                'humid': 'Данные о погоде не найдены',
                'press': 'Данные о погоде не найдены',
                'vis': 'Данные о погоде не найдены'
            }

        return result_data