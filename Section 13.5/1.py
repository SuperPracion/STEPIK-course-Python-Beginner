def is_valid_triangle(side1, side2, side3):
    flag_triangel = False
    if (side1 < side2 + side3) and (side2 < side3 + side1) and (side3 < side1 + side2):
        flag_triangel = True

    return flag_triangel

# считываем данные
a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))