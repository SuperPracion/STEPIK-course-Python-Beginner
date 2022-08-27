numbers = [8, 9, 10, 11]

numbers[1] = 17

for i in range(4, 7):
    numbers.append(i)

del numbers[0]
numbers += numbers.copy()
numbers.insert(3, 25)
print(numbers)