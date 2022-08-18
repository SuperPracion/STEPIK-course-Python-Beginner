in_num = int(input())
sum_fact = 0

for i in range(1, in_num + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum_fact += fact

print(sum_fact)