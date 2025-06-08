numbers = [1, 5, 8, 10, 13, 17]
answer = []
#будемо міняти парні числа на наступні не парні
for i in range(0, len(numbers)):
    number = numbers[i]
    if number % 2 == 0:
        answer.append(number+1)
    else:
        answer.append(number)
    
print (answer)