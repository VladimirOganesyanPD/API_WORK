"""
Модуль, содержащий описание класса Vacancy для представления информации о вакансии.
"""


class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __repr__(self):
        return f"Vacancy(title={self.title}, salary={self.salary})"

    def __lt__(self, other):
        return self.salary < other.salary

    @classmethod
    def cast_to_object_list(cls, vacancies_json):
        vacancies = []
        for vacancy_json in vacancies_json:
            title = vacancy_json.get('name', '')
            link = vacancy_json.get('alternate_url', '')
            salary = vacancy_json.get('salary', 'Зарплата не указана')
            description = vacancy_json.get('description', '')
            vacancies.append(cls(title, link, salary, description))
        return vacancies
