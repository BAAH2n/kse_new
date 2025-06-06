list = [2, 3, 8, 9, 10, 11]
new_list = []
condition = float(input('What is your condition? '))

for i in list:
    if i > condition:
        new_list.append(i)

print(new_list)