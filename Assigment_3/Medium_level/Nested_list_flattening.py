lIst = [1, 2, 3, [5, 6, 9], 4, 10]
new_list = []

for i in lIst:
    if isinstance(i, list):
        for j in i:
            new_list.append(j)
    else:
        new_list.append(i)
print(new_list)