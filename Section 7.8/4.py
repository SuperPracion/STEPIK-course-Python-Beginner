height_triangel = int(input())

for i in range(1, height_triangel // 2 + 1):
    print('*' * i)

print('*' * (height_triangel // 2 + 1)) # print middle height

for i in range(height_triangel // 2, 0, -1):
    print('*' * i)
