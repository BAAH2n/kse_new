numbers1 = [2,3,4,5,6,7,8,9,10]
numbers2 = [21,22,23,24,25,26,27,28,29,30,31,32,33]
answer = []

for i in numbers1:
    if i % 5 == 0:
        answer.append(i)
for i in numbers2:
    if i % 5 == 0:
        answer.append(i)
print(answer)