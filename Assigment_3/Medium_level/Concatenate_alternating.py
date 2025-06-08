list1 = ["яблуко", "машина", "будинок", "сонце", "книга"]
list2 = ["рідина", "стілець", "комп'ютер", "річка", "дерево"]
answer = []

for i in range (0, len(min(list1, list2))):
    answer.append(list1[i])
    answer.append(list2[i])
print (answer)