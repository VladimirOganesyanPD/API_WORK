"""
Модуль для работы с API платформы hh.ru.
Содержит класс для работы с API и получения информации о вакансиях.
"""

import requests
from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HeadHunterAPI(VacancyAPI):
    def get_vacancies(self, search_query):
        url = f"https://api.hh.ru/vacancies"
        params = {'text': search_query}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return []
