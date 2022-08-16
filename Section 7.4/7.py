count_services = int(input())
sum_coins = 0

while count_services != 0:
    if count_services >= 25:
        count_services -= 25
    elif count_services >= 10:
        count_services -= 10
    elif count_services >= 5:
        count_services -= 5
    else:
        count_services -= 1

    sum_coins += 1

print(sum_coins)
