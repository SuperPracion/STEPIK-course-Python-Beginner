binary_list = [int(num) for num in input()[::-1]]
decimal_answer = 0

for num in range(len(binary_list)):
    decimal_answer += binary_list[num] * (2 ** num)


print(decimal_answer)