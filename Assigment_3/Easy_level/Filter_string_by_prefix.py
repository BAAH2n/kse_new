list = ['розчин', "розійшовся", "фрукт", "розтин"]
answer = []
prefix = str(input('Введіть префікс: '))

words = []
for i in list:
    if i.startswith(prefix) is True:
        answer.append(i)
print (answer)