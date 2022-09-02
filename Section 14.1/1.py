def draw_triangle():
    middle = 15

    for hight in range(1, middle + 1, 2):
        print(' ' * ((middle - hight) // 2) + '*' * hight)

draw_triangle()