list = [2, 3, 8, 9, 10, 11]
number = int(input("First numbers of the list: "))
sum = 0

if number > len(list):
    print("Your number is bigger than number of elenemts in the list")
else:
    for i in range(0, number):
        sum += list[i]
    print(sum)