import requests
from random import randint
from datetime import datetime, timedelta
from googletrans import Translator

from loader import logger

from config_data.bot_config import NASA_API, DOG_API
translator: Translator = Translator()


class SpacePhoto:

    def __init__(self):
        self.__api_id: str = NASA_API
        self.__start_date: datetime = datetime.now() - timedelta(days=365)

    def __random_date(self) -> str:
        """
        Получение даты

        :return: form_date
        """
        rand_date: datetime = self.__start_date + timedelta(days=randint(0, 365))
        form_date: str = rand_date.strftime('%Y-%m-%d')

        return form_date

    def __get_data(self) -> dict[str, str]:
        """
        Получение данных NASA

        :return: response
        """
        nasa_url: str = f'https://api.nasa.gov/planetary/apod?api_key={self.__api_id}&date={self.__random_date()}'
        response: requests = requests.get(nasa_url)

        return response.json()

    def get_photo(self) -> [str, str]:
        """
        Получение фотографии из космоса и её описания

        :return: spase_photo, russian_title
        """
        spase_photo: str = self.__get_data()['url']
        spase_title: str = self.__get_data()['title']
        russian_title: str = translator.translate(spase_title, dest='ru').text

        return spase_photo, russian_title


class DogBreed:

    def __init__(self):
        self.__api_id: str = DOG_API

    def breed_pool(self) -> str:
        """
        Получение породы собаки

        :return: dog_breed
        """
        dog_url = "https://api.thedogapi.com/v1/breeds"
        headers = {"x-api-key": self.__api_id}
        response = requests.get(dog_url, headers=headers)

        for breed in response.json():
            print(breed)

        return response.json()