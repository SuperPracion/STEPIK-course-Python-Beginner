range_num = int(input())
nums_sum = 0
flag_action = True

for i in range(1, range_num + 1):
    if flag_action:
        nums_sum += i
    else:
        nums_sum -= i
        
    flag_action = not flag_action
    
print(nums_sum) 