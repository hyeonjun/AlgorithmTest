num = input()
if num[0] == '0' and num[1] == 'x':
    print(int(num, 16))
elif num[0] == '0':
    print(int(num, 8))
else:
    print(int(num))