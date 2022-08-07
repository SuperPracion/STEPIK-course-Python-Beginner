# put your python code here
a1, b1, a2, b2 = [int(input()) for _ in range(4)]

if b1 == a2 or a1 == b2:
    if b1 == a2:
        print(b1)
    else:
        print(a1)
elif (a1 <= a2 < b1 < b2) or (a2 <= a1 < b2 < b1):
    if (a1 <= a2 < b1 < b2):
        print(a2, b1)
    else:
        print(a1, b2)
elif a1 < a2 < b2 <= b1:
    print(a2, b2)
elif (a2 < a1 < b1 <= b2) or (a1 == a2 and b1 == b2):
    print(a1, b1)
else:
    print('пустое множество')