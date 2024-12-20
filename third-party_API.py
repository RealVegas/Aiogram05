import requests
from datetime import datetime, timedelta
from googletrans import Translator

translator: Translator = Translator()
# translated_text: str = translator.translate(message.text, dest='en').text

from config_data.bot_config import NASA_API


class GetSpacePhoto:

    def __init__(self):
        self.__api_id = NASA_API
        self.__end_date = datetime.now()
        self.__start_date = self.__end_date - timedelta(days=365)

    def __get_date(self) -> str:
        """
        Получение даты

        :return: date
        """
        date = self.__start_date.strftime('%Y-%m-%d')
        return date