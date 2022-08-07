color1 = input()
color2 = input()

if color1 not in ('красный', 'синий','желтый') or color2 not in ('красный', 'синий','желтый'):
    print('ошибка цвета')
elif color1 == 'красный' or color2 == 'красный':
    if color1 == 'синий' or color2 == 'синий':
        print('фиолетовый')
    elif color1 == 'желтый' or color2 == 'желтый':
        print('оранжевый')
    else:
        print('красный')
elif color1 == 'синий' or color2 == 'синий':
    if color1 == 'красный' or color1 == 'красный':
        print('фиолетовый')
    elif color1 == 'желтый' or color2 == 'желтый':
        print('зеленый')
    else:
        print('синий')
elif color1 == 'желтый' or color2 == 'желтый':
    if color1 == 'красный' or color1 == 'красный':
        print('оранжевый')
    elif color1 == 'синий' or color2 == 'синий':
        print('зеленый')
    else:
        print('желтый')
