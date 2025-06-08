list = [2, 3, 8, 9, 10, 11]
new_list = []
condition = float(input('What is your condition X? '))
condition_2 = float(input('What is your condition Y? '))

for i in list:
    if i % condition == 0 and i % condition_2 != 0:
        new_list.append(i)
print (new_list)