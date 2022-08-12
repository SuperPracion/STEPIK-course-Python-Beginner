citys = [input() for _ in range(3)]

print(min(citys, key=len))
print(max(citys, key=len))