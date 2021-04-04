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
from hw10_task2_exception import *
import string


class UserToken:

    user_database = {}

    def __str__(self):
        print(self.generate_random_string())

    def register(self, name: str, email: str, password: str):
        try:
            if self.check_name(name) is False:
                raise ErrorName('Invalid name')

            if self.check_email(email) is False:
                raise ErrorEmail('invalid email')

            if self.check2_email(email) is False:
                raise ErrorEmail2('invalid email')

            if self.check_password(password) is False:
                raise ErrorPassword('Invalid password')

            if email in self.user_database:
                raise Error('User is registered')

            raise UserDataBase
        except UserDataBase:
            self.user_database.update({email: password})
        return 200

    def login_in(self, email: str, password: str):
        if email in self.user_database and password in self.user_database.values():
            return UserToken.__str__(self)
        else:
            raise ErrorLoginPassword('Invalid login or password')

    @staticmethod
    def generate_random_string():
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(10))
        return rand_string

    @staticmethod
    def check_name(name: str):
        if 3 < len(name) < 12:
            for el in name:
                if 123 > ord(el) > 97 or 90 > ord(el) > 65:
                    return True
        return False

    @staticmethod
    def check_email(email: str):
        for el in email:
            if 123 > ord(el) > 97 or 58 > ord(el) > 47:
                return True
            return False

    @staticmethod
    def check2_email(email: str):
        count = 0
        for el in email:
            if el == '@' or el == '.':
                count += 1
        if count == 2:
            return True
        return False

    @staticmethod
    def check_password(password: str):
        count = 0
        count1 = 0
        if len(password) >= 8:
            for el in password:
                if el.isdigit() is True:
                    count += 1
                if el.isalpha() is True:
                    count1 += 1
        if count > 1 and count1 > 1:
            return True
        return False


user = UserToken()
user.register('Bohdan', 'bogdan@gmail.com', 'Zaqwerty123')
print(user.user_database)




