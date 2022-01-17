n = input()
if len(n) == 3:
    if n[:2] == '10':
        a, b = n[:2], n[2:]
    elif n[1:] == '10':
        a, b = n[0], n[1:]
elif len(n) == 4:
    a, b = n[:2], n[2:]
else:
    a, b = n[0], n[1]
print(int(a)+int(b))