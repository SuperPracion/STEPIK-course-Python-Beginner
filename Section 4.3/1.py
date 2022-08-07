n_zoom, k_flash = [int(input()) for _ in range(2)]

if n_zoom > k_flash:
    print('NO')
elif n_zoom < k_flash:
    print('YES')
else:
    print('Don't know')