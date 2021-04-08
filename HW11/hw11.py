# 1. double_result
# This decorator function should return the result of another function multiplied by two

def double_result(func):
    # return function result multiplied by two
    def inner(a, b):
        print(f'Result - ({a} + {b}) * 2')
        return func(a, b) * 2

    return inner


print(f'# 1. double_result \n')


def add(a, b):
    print(f'Result - {a} + {b}')
    return a + b


print(add(5, 5), '\n')  # 10


@double_result
def add(a, b):
    return a + b


print(add(5, 5), '\n')  # 20


# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    # if args passed to func are not odd - return "Please use only odd numbers!"
    def inner(*args):
        for element in args:
            if element % 2 == 0:
                print(f'Result - {args}')
                return 'Please use only odd numbers!'
        return func(*args)

    return inner


print(f'# 2. only_odd_parameters\n')


@only_odd_parameters
def add(a, b):
    print(f'Result - {a} + {b}')
    return a + b


print(add(5, 5), '\n')  # 10
print(add(4, 4), '\n')  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    print(f'Result - {a} * {b} * {c} * {d} * {e}')
    return a * b * c * d * e


print(multiply(5, 5, 5, 7, 9), '\n')
print(multiply(5, 5, 4, 8, 2), '\n')


# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):


def logged(func):
    # log function arguments and its return value
    def inner(*args, **kwargs):
        print(f'Result - {func(*args, **kwargs)}\n')
        return func(*args, **kwargs)
    return inner


print(f'# 3.* logged\n')


@logged
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


func(4, 4, 4)


# you called func(4, 4, 4)
# it returned 6


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    # put code here
    def decorator_type(func):
        def inner(name):
            if isinstance(name, correct_type):
                return func(name)
            else:
                print(f'Wrong Type: {type(name)}\n')
        return inner
    return decorator_type


print(f'# 4. type_check \n')


@type_check(int)
def times2(num):
    return f'{num * 2}\n'


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return f'{word[0]}\n'


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
