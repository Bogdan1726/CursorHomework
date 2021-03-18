# 1.
class Laptop:
    """
    Make the class with composition.
    """
    def __init__(self, model_laptop, battery_manufacturer):
        self.battery = Battery(battery_manufacturer)
        self.model_laptop = model_laptop

    def __str__(self):
        return f'Laptop model - {self.model_laptop}, and battery - {self.battery}'


class Battery:
    """
    Make the class with composition.
    """
    def __init__(self, battery_manufacturer):
        self.battery_manufacturer = battery_manufacturer

    def __str__(self):
        return f'{self.battery_manufacturer}'


battery = Laptop('Lenovo', 'Tesla')
print(battery)

# Laptop model - Lenovo, and battery - Tesla


# 2.
class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, model_guitar):
        self.model_guitar = model_guitar

    def __str__(self):
        return f'{self.model_guitar}'


class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self, model_guitar, number_of_strings):
        self.model_guitar = model_guitar
        self.number_of_strings = number_of_strings

    def __str__(self):
        return f'{self.model_guitar} - {self.number_of_strings} strings'


guitar = Guitar('Yamaha')
guiter_string = GuitarString(guitar, '7')
print(guiter_string)


# Yamaha - 7 strings


# 3
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """
    @staticmethod
    def add_nums(num1, num2, num3):
        return num1 + num2 + num3


summa = Calc.add_nums(5, 6, 7)
print(summa)


# 18


# 4*.
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['tomato', 'cucumber'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
print(f'pasta_1.ingredients will equal to {pasta_1.list_of_ingredients}')
pasta_2 = Pasta.bolognaise()
print(f'pasta_2.ingredients will equal to {pasta_2.list_of_ingredients}')


# pasta_1.ingredients will equal to['tomato', 'cucumber']
# pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']


# 5*.
class Concert:
    """"
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitors


concert = Concert()
Concert.max_visitors_num = 50
concert.visitors_count = 1000
print(concert.visitors_count)


# 50


# 6.
import dataclasses


@dataclasses.dataclass()
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


note = AddressBookDataClass(1, 'Bohdan', '0939804334', 'city.Dnipro', 'bogdan24ro@gmail.com', '1993', 27)
print(note)
note.key = 2
print(note)


# AddressBookDataClass(key=1, name='Bohdan', phone_number='0939804334', address='city.Dnipro',
# email='bogdan24ro@gmail.com', birthday='1993', age=27)

# AddressBookDataClass(key=2, name='Bohdan', phone_number='0939804334',
# address='city.Dnipro', email='bogdan24ro@gmail.com', birthday='1993', age=27)


# 7. Create the same class (6) but using NamedTuple
import collections

AddressBookDataClass = collections.namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address',
                                                                       'email', 'birthday', 'age'])

note2 = AddressBookDataClass(1, 'Bohdan', '0939804334', 'city.Dnipro', 'bogdan24ro@gmail.com', '1993', 27)
print(note2)


# AddressBookDataClass(key=1, name='Bohdan', phone_number='0939804334', address='city.Dnipro',
# email='bogdan24ro@gmail.com', birthday='1993', age=27)


# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key={self.key}, name={self.name}, phone_number={self.phone_number},' \
               f' address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})'


address = AddressBook(1, 'Bohdan', '0939804334', 'city.Dnipro', 'bogdan24ro@gmail.com', '1993', 27)
print(address)


# AddressBook(key=1, name=Bohdan, phone_number=0939804334, address=city.Dnipro,
# email=bogdan24ro@gmail.com, birthday=1993, age=27)


# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person = Person()
print(person.age)
Person.age = 27
print(person.age)


# 36
# 27

# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(1, 'Bogdan')
student.email = 'bogdan24ro@gmail.com'
student_email = getattr(student, 'email')
print(student_email)

# bogdan24ro@gmail.com


# 11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        return self._temperature * 1.8 + 32


# create an object
obj = Celsius(2)

print(f'{obj.fahrenheit} - Fahrenheit')

# 35.6 - Fahrenheit
