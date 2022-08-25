# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#
# for color in range(len(rainbow)):
#     match rainbow[color]:
#         case 'Green':
#             rainbow[color] = 'Зеленый'
#         case 'Violet':
#             rainbow[color] = 'Фиолетовый'
#
# print(rainbow)

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

rainbow[3] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'

print(rainbow)
