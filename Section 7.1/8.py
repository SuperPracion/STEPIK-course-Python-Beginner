population = float(input())
reproduction = (100 + float(input())) / 100
days = int(input())

for day in range(1, days + 1):
    print(day, population)
    population = population * reproduction