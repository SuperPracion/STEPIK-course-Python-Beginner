call_number = input()

flag_is_ok = True

if call_number.count('-') < 2:
    flag_is_ok = False

call_number = call_number.split('-')

if len(call_number) == 4:
    if call_number[0] != '7' and len(call_number[1]) > 4 or len(call_number[2]) > 4 or len(call_number[3]) > 5:
        flag_is_ok = False

elif len(call_number) == 3:
    if len(call_number[0]) != 3 or len(call_number[1]) != 3 or len(call_number[2]) != 4:
        flag_is_ok = False

for num in call_number:
    if not num.isdigit():
        flag_is_ok = False
        break

print('YES' if flag_is_ok else 'NO')