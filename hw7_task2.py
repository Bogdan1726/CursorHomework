# Task 2
from pickle import loads
with open("task2", "rb") as file:
    summa = 0
    lis = loads(file.read())
    for i in range(len(lis)):
        summa += int(lis[i])
    print(summa)
    # 3563
    print(summa / len(lis))
    # 187.52631578947367



