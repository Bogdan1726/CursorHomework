# Task 1
# 1
with open("task1.txt", "r") as file:
    dic = {}
    content = file.readlines()
    for i in range(0, len(content), 2):
        content[i] = content[i].replace("\n", "")
        content[i + 1] = content[i + 1].replace("\n", "")
        dic.update({content[i]: content[i + 1]})
    print(dic)


# 2
with open('homework_task1_2.txt', 'w') as file:
    for element in dic.values():
        file.write(f'{element} ')


