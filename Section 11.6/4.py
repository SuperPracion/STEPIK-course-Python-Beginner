len = int(input().replace('#', ''))

for _ in range(len):
    inp_str = input()
    find_symbdol = inp_str.find('#')
    print(inp_str.rstrip() if find_symbdol == -1 else inp_str[find_symbdol:].rstrip())
