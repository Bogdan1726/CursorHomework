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


import random


class Error(Exception):
    pass


class UserToken:

    user_database = {'test@gmail.com': 'Bob', 'test1@gmail.com': 'Marta',
                     'test2@gmail.com': 'Elizabet'}

    def register(self, values):
        if values not in self.user_database:
            self.user_database.update([values])

    def login_in(self, values):
        if values in self.user_database:
            return UserToken


user = UserToken()
print(user.login_in('test@gmail.com'))
