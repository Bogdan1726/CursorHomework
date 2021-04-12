"""
3. Use Pool.apply() to get the row wise common items in list_a and list_b.
list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
"""

from multiprocessing import Pool

unique_values = []


def intersection_value(a, b):
    set_1 = set(a)
    set_2 = set(b)
    return list(set_1.intersection(set_2))


list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]

pool = Pool()
for i in range(len(list_a)):
    unique_values.append(pool.apply(intersection_value, [list_a[i], list_b[i]]))
print(unique_values)



