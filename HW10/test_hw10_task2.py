"""
Task3
Напишіть тести до модуля реєстрації юзера (без фласк АРІ, просто окремий клас)
тести повинні перевіряти чи відповідає пароль пошта і ім'я вимогам,
перевіряти чи юзера з таким іменем не має в базі
якщо юзер створений то назад отримуємо строку "200", інакше модуль реєстрації кидатиме ексепшини
 (ексепшини потрібно написати свої)

тести до модуля авторизації юзера
метод авторизації отримує пошту і пароль і звіряє чи є такі в базі данних (за бд можете використати словник)
якщо дані введені вірно і юзер існує то назад повертаєтсья обєкт класу UserToken (майже пустий клас,
містить тільки аргумент строку яка задається рандомним набором символів)

Після написання тестів, реалізуйте ваші методи реєстрації і авторизаії
"""


import unittest

from hw10_task2 import UserToken
from hw10_task2_exception import *


class TestUserToken(unittest.TestCase):

    def setUp(self) -> None:
        self.user = UserToken()

    def test_register(self):
        with self.assertRaises(ErrorPassword):
            self.user.register('Ivan', 'ivan@gmail.com', 'Zaqwerty')
        with self.assertRaises(ErrorName):
            self.user.register('Iva', 'ivan@gmail.com', 'Zaqwerty123')
        with self.assertRaises(ErrorEmail2):
            self.user.register('Ivan', 'ivangmail.com', 'Zaqwerty123')
        with self.assertRaises(ErrorEmail):
            self.user.register('Ivan', '@gmail.com', 'Zaqwerty123')
        self.assertEqual(self.user.register('Bohdan', 'bogdan24@gmail.com', 'Zaqwerty123'), 200)

    def test_login_in(self):
        with self.assertRaises(ErrorLoginPassword):
            self.user.login_in('bo@gmail.com', 'Zaqwerty')
        self.user.login_in('bogdan@gmail.com', 'Zaqwerty123')

    def tearDown(self) -> None:
        print('tearDown')


if __name__ == '__main__':
    unittest.main(verbosity=2)


