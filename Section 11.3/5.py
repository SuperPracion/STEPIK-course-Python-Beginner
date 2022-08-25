divisors = []
int_input = int(input())

for divider in range(1, int_input + 1):
    if int_input % divider == 0:
        divisors.append(divider)

print(divisors)