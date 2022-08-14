first_num = 1
back_num = 0

for _ in range(int(input())):
   print(first_num)
   back_num, first_num = first_num, back_num + first_num
