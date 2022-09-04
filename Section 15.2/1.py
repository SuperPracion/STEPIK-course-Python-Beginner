from math import *

def number_attempts(num):
    num = int(ceil(log2(num)))
    return num

num = int(input())
print(number_attempts(num))