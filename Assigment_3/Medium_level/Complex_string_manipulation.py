text = input('Введіть текст, з якого хочете дістати великі літери: ')
up_letters = []

for i in text:
    if i.isupper():
        up_letters.append(i)
print("Великі літери у реченні: ", up_letters)