from api.vacancy_api import HeadHunterAPI
from models.vacancy import Vacancy
from storage.vacancy_saver import JSONSaver


def filter_vacancies(vacancies, filter_words):
    filtered_vacancies = []
    filtered_reasons = []  # Список причин фильтрации

    for vacancy in vacancies:
        reasons = []  # Причины фильтрации для каждой вакансии

        # Если объект - словарь, создаем экземпляр класса Vacancy
        if isinstance(vacancy, dict):
            vacancy = Vacancy(**vacancy)

        # Проверяем наличие ключевых слов в описании
        if vacancy.description is not None:
            if not all(word in vacancy.description for word in filter_words):
                reasons.append("Отсутствие ключевых слов в описании")

        # Проверяем наличие атрибута 'salary' и его корректность
        if not hasattr(vacancy, 'salary') or (not isinstance(vacancy.salary, int) and not isinstance(vacancy.salary, str)):
            reasons.append("Отсутствие или некорректное указание зарплаты")

        # Если есть причины фильтрации, добавляем в список причин и пропускаем вакансию
        if reasons:
            filtered_reasons.append((vacancy, reasons))
        else:
            filtered_vacancies.append(vacancy)

    return filtered_vacancies, filtered_reasons


def get_vacancies_by_salary(vacancies, salary_range):
    min_salary, max_salary = map(int, salary_range.split('-'))
    return [vacancy for vacancy in vacancies if
            vacancy.salary.isdigit() and min_salary <= int(vacancy.salary) <= max_salary]


def sort_vacancies(vacancies):
    return sorted(vacancies)


def get_top_vacancies(vacancies, n):
    return vacancies[:n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(f"Title: {vacancy.title}")
        print(f"Link: {vacancy.link}")
        print(f"Salary: {vacancy.salary}")
        print(f"Description: {vacancy.description}")
        print("-" * 50)


def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 20000-150000

    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    filtered_vacancies, filtered_reasons = filter_vacancies(vacancies_list, filter_words)
    print("Отфильтрованные вакансии:")
    print_vacancies(filtered_vacancies)

    if filtered_reasons:
        print("\nВакансии, которые не прошли фильтрацию и причины:")
        for vacancy, reasons in filtered_reasons:
            print(f"Вакансия: {vacancy.title}")
            print("Причины фильтрации:")
            for reason in reasons:
                print(f"- {reason}")
            print()

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print("\nТоп вакансий:")
    print_vacancies(top_vacancies)

if __name__ == "__main__":
    user_interaction()