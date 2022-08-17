# this is a code review class
n = int(input())
product = 1
while n:
    digit = n % 10
    product *= digit
    n //= 10
print(product)