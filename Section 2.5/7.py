in_num = int(input())
f_num = in_num // 100
s_num = (in_num % 100) // 10
t_num = in_num % 10

print("Сумма цифр =", f_num + s_num + t_num)
print("Произведение цифр", f_num * s_num * t_num)