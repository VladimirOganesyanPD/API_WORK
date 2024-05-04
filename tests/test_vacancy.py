import unittest

class TestVacancyClass(unittest.TestCase):
    def test_cast_to_object_list(self):
        # Mock response from API
        vacancies_json = [
            {'name': 'Python Developer', 'alternate_url': 'http://example.com', 'salary': '100000-150000', 'description': 'Python developer job description'},
            {'name': 'Java Developer', 'alternate_url': 'http://example.com', 'salary': '80000-120000', 'description': 'Java developer job description'},
        ]
        vacancies = Vacancy.cast_to_object_list(vacancies_json)
        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0].title, 'Python Developer')