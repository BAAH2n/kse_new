string1 = "Сонце світило яскраво над морем."
string2 = "Вона читала книжку на лавці в парку 'Наталка'."
string3 = "Після дощу з’явилася яскрава веселка."

strings = [string1, string2, string3]
count = 0

x = int(input('Введіть число для порівняння: '))

for i in strings:
    if len(i) > x:
        count += 1
print (count)

