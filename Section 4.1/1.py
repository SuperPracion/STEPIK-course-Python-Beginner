f_password = input()
input_password = input()

if f_password == input_password:
    print("Пароль принят")
else:
    print("Пароль не принят")

# print("Пароль принят" if (f_password == input_password) else "Пароль не принят")

# print("Пароль принят" if (input() == input()) else "Пароль не принят")