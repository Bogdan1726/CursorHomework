"""Task 1
Напишіть калькулятор в якого будуть реалізовані операції додавання, віднімання, множення, ділення, піднесення в степінь,
взяття з під кореня, пошук відсотку від числа

Огорніть в конструкцію try... except... потенційно "небезпечні" місця, наприклад отримання числа і приведення до типу
даних або інструкції математичних операцій

заповніть ваш скрипт логами
Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
+ логи з помилками
причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
лог файл завжди відкриваєтсья в режимі дозапису.
так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки"""

import logging

log_template = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s'
logging.basicConfig(level=logging.DEBUG, filename="test.log", filemode="a", format=log_template)


operations = ['+', '-', '*', '/', '**', 'scrt', '%']


def operation(values):
    if values == '+':
        try:
            return summa(int(input('enter the num1: ')), int(input('enter the num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'You entered not a number'
    if values == '-':
        try:
            return difference(int(input('enter the num1: ')), int(input('enter the num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'You entered not a number'
    if values == '*':
        try:
            return multiplication(int(input('enter the num1: ')), int(input('enter the num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'No You entered not a number'
    if values == '/':
        try:
            return division(int(input('enter the num1: ')), int(input('enter the num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'You entered not a number'
    if values == '**':
        try:
            return exponentiation(int(input('enter the num1: ')), int(input('enter the num2: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'No You entered not a number'
    if values == 'sqrt':
        try:
            return sqrt1(int(input('enter the num: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'No You entered not a number'
    if values == '%':
        try:
            return percentage_of_the_number(int(input('enter the percent: ')), int(input('enter the num: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'No You entered not a number'


def summa(num1, num2):
    logging.info('Returns summa two numbers')
    return f'Result: {num1} + {num2} = {num1 + num2}'


def difference(num1, num2):
    logging.info('Returns difference two numbers')
    return f'Result: {num1} - {num2} = {num1 - num2}'


def multiplication(num1, num2):
    logging.info('Returns multiplication two numbers')
    return f'Result: {num1} * {num2} = {num1 * num2}'


def division(num1, num2):
    try:
        logging.info('Returns division two numbers')
        return f'Result: {num1} / {num2} = {num1 / num2}'
    except ZeroDivisionError:
        logging.error('ZeroDivisionError', exc_info=True)
        return 'You cannot divide by zero'


def exponentiation(num1, num2):
    logging.info('Returns exponentiation')
    return f'Result: {num1} ** {num2} = {num1 ** num2}'


def sqrt1(num):
    from math import sqrt
    logging.info('Returns square root numbers')
    return f'Result: {num} = {sqrt(num)}'


def percentage_of_the_number(percent, num2):
    logging.info('Returns percentage of the number')
    return f'Result: {percent}% from {num2} = {num2/100 * percent} '


while True:
    inputs = input(f'Operation: ')
    if inputs == 'exit':
        logging.info('Exit from program')
        print('Goodbye')
        break
    if inputs in operations:
        print(operation(inputs))
    else:
        logging.warning('Wrong operation')
        print(f'Sorry, this operation is not in the list of available ones. '
              f'Choose from these - {operations}')


"""Task 2
Напишіть клас робота пилососа
в ініт приймається заряд батареї, заповненість сміттєбака і кількість води

реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
(в цих функціях повинні стояти прніти "wash" і "vacuum cleaner" відповідно),
також на кожній ітерації прінтиться "move"
+ на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
(задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
а кількість сміття збільшується

Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0,
 кількість сміття більша ніж певне число
опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій 
і зупиняється,
якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)
можете придумати ще свої ексепшини і як їх опрацьовувати """
