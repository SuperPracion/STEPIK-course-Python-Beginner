def is_valid_password(password):
    password = password.split(':')
    flag_good_password = True

    if len(password) > 3:
        return False

    a, b, c = [num for num in password]

    if a != a[::-1]:
        flag_good_password = False

    if sum(1 for i in range(1, int(b) + 1) if int(b) % i == 0) != 2:
        flag_good_password = False

    if int(c) % 2 != 0:
        flag_good_password = False

    return flag_good_password

psw = input()

print(is_valid_password(psw))