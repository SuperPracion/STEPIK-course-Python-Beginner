num1, num2 = [int(input()) for _ in range(2)]
operation = input()

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
else:
    if num1 == 0 == num2:
        print('На ноль делить нельзя!')
    else:
        print(num1 / num2)