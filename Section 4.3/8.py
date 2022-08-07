ball = int(input())

if ball == 0:
    print('зеленый')
elif 1 <= ball <= 10:
    if ball % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= ball <= 18:
    if ball % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= ball <= 28:
    if ball % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= ball <= 36:
    if ball % 2 == 0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')
