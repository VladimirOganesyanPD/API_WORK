import unittest

from models.vacancy import Vacancy
from storage.vacancy_saver import JSONSaver


class TestJSONSaverClass(unittest.TestCase):
    def setUp(self):
        self.json_saver = JSONSaver(filename='test_vacancies.json')

    def tearDown(self):
        import os
        os.remove('test_vacancies.json')

    def test_add_and_delete_vacancy(self):
        vacancy = Vacancy("Python Developer", "http://example.com", "100000-150000", "Python developer job description")
        self.json_saver.add_vacancy(vacancy)
        self.assertEqual(len(self.json_saver.vacancies), 1)

        self.json_saver.delete_vacancy(vacancy)
        self.assertEqual(len(self.json_saver.vacancies), 0)

    def test_get_vacancies_by_criteria(self):
        vacancy1 = Vacancy("Python Developer", "http://example.com", "100000-150000", "Python developer job description")
        vacancy2 = Vacancy("Java Developer", "http://example.com", "80000-120000", "Java developer job description")
        self.json_saver.add_vacancy(vacancy1)
        self.json_saver.add_vacancy(vacancy2)

        filtered_vacancies = self.json_saver.get_vacancies_by_criteria(['Python'])
        self.assertEqual(len(filtered_vacancies), 1)
        self.assertEqual(filtered_vacancies[0]['title'], 'Python Developer')