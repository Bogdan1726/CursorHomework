#1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e), sep='\n')

#2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

#3. Define the type of each object from step 1.
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e), sep='\n')

#4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int), isinstance(str_b, str), isinstance(set_c, set), isinstance(lst_d, list), isinstance(dict_e, dict), sep='\n')

#5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(3, 5))

#6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(3, 5))

#7. By using keyword arguments into the curly braces.
print("Anna has {apple} apples and {peach} peaches.".format(apple=3, peach=5))

#8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(3, 5))

#9. With f-strings and variables
apple = 5
peach = 7
print(f"Anna has {apple} apples and {peach} peaches.")

#10. With % operator
print("Anna has %s apples and %s peaches." % (apple, peach))

#11*. With variable substitutions by name (hint: by using dict)
data_dict = {"a": apple, "b": peach}
print("Anna has %(a)s apples and %(b)s peaches." % data_dict)

#12. Convert (1) to list comprehension
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]

#13. Convert (2) to regular for with if-else
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num//2)
    else:
        lst.append(num*10)
print(lst)

#14. Convert (3) to dict comprehension.
dict_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}

#15*. Convert (4) to dict comprehension.
dict_comprehension_1 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}

#16. Convert (5) to regular for with if.
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print(d)

#17*. Convert (6) to regular for with if-else.
d1 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d1[x] = x ** 3
    else:
        d1[x] = x
print(d1)

#18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y

#19*. Convert (8) to regular function
def foo1(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

#20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

#21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))

#22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))

#23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list(map(lambda a, b: a + b, list_A, list_B)))

#24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce
print(reduce(lambda x, y: x + y, lst_to_sort))

#25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda elem: (elem % 2 == 1), lst_to_sort)))

#26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
print(list(filter(lambda x: x < 0, b)))

#27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

print(list(filter(lambda x: x in list_2, list_1)))