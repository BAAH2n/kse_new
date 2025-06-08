numbers = [3, 7, 2, 5, 3, 9, 7, 2, 8, 5, 1, 9, 7, 4, 6, 7, 9, 1, 7]
frequency = {}

sorted_by_descending = sorted(numbers, reverse = True)
print(sorted_by_descending)
for i in numbers:
    if i in frequency:
        frequency[i] = frequency.get(i) + 1
    else:
        frequency[i] = 1
sorted_by_frequency = sorted(sorted_by_descending, key=lambda x: frequency[x])
print(sorted_by_frequency)