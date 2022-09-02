from math import *

def compute_binom(n, k):
    binom_effect = (factorial(n)) / (factorial(k) * factorial(n - k))
    return int(binom_effect)

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))