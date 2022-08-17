# this is a code review class
count = 0
p = 1
for _ in range(10):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count, p, sep='\n')
else:
    print('NO')
