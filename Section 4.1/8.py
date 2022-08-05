years_old = int(input())

if years_old <= 13:
    print('детство')
elif 14 <= years_old <= 24:
    print('молодость')
elif 25 <= years_old <= 59:
    print('зрелость')
else:
    print('старость')