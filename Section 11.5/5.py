ip_address = input().split('.')

for num in ip_address:
    if int(num) < 0 or int(num) > 256:
        print('НЕТ')
        break
else:
    print('ДА')
