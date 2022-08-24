str_input = input()
x_ind = str_input.find('h')
y_ind = str_input.rfind('h')

print(str_input[:x_ind + 1] + str_input[y_ind - 1:x_ind: -1] + str_input[y_ind:])