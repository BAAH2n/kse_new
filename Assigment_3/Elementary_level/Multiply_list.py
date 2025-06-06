list = [2, 3, 8, 9, 10, 11]
new_list = []
number = float(input("What number do you want to multiply by?: "))

for i in list:
    new_list.append(i*number)
print(new_list)