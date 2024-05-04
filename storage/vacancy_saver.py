"""
Модуль для работы с сохранением и загрузкой информации о вакансиях в JSON-файл.
Содержит класс для сохранения и удаления вакансий.
"""

import json
from abc import ABC, abstractmethod

class VacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        pass

class JSONSaver(VacancySaver):
    def __init__(self, filename='vacancies.json'):
        self.filename = filename
        self.vacancies = self.load_vacancies()

    def load_vacancies(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vars(vacancy))
        self._save_to_json()

    def delete_vacancy(self, vacancy):
        self.vacancies = [v for v in self.vacancies if v != vars(vacancy)]
        self._save_to_json()

    def _save_to_json(self):
        with open(self.filename, 'w') as file:
            json.dump(self.vacancies, file)

    def get_vacancies_by_criteria(self, criteria):
        filtered_vacancies = []
        for vacancy in self.vacancies:
            if all(word in vacancy['description'] for word in criteria):
                filtered_vacancies.append(vacancy)
        return filtered_vacancies