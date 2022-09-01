def is_password_good(password):
    flag_good_password = True

    if len(password) < 8:
        flag_good_password = False

    if sum(1 for c in password if c.isupper()) < 1:
        flag_good_password = False

    if sum(1 for c in password if c.islower()) < 1:
        flag_good_password = False

    if sum(1 for c in password if c.isdigit()) < 1:
        flag_good_password = False

    return flag_good_password

txt = input()

# вызываем функцию
print(is_password_good(txt))