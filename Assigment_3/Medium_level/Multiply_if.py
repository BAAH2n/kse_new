numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
answer = []

x=float(input("Введіть число для порівняння: "))
y=float(input("Введіть число на яке буде множитися: "))

for i in numbers:
    if i > x:
        answer.append(i*y)
print(answer)