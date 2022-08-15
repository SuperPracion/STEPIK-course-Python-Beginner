in_str = input()
sum_str_without_stop = 0

while in_str not in ('стоп', 'хватит', 'достаточно'):
    sum_str_without_stop += 1
    in_str = input()
    
print(sum_str_without_stop)