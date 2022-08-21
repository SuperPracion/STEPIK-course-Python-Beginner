def cubes():
    for a in range(1, 50):
        a_cube = a ** 3
        for b in range(1, 50):
            b_cube = b ** 3
            for c in range(1, 50):
                c_cube = c ** 3
                for d in range(1, 50):
                    d_cube = d ** 3
                    if a_cube + b_cube == c_cube + d_cube:
                        if a not in (b, c, d) and b not in (a, c, d) and c not in (a, b, d) and d not in (a, b, c):
                            print(a_cube + b_cube)

cubes()
