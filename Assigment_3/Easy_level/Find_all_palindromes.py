list = [123321, 'eye', 'Hello', 858, 'Car']
answer = []

for i in list:
    if str(i) == str(i)[ : :-1]:
        answer.append(i)
print(answer)