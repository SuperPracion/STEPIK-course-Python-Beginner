def draw_triangle(fill, base):
    middle = base // 2
    for i in range(1, middle + 2):
        print(fill * i)

    for i in range(middle, 0, -1):
        print(fill * i)

fill = input()
base = int(input())

draw_triangle(fill, base)