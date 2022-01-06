string = input()
a, b = 0, 0
for i in range(len(string)-2):
    if string[i:i+3] == 'JOI':
        a += 1
    elif string[i:i+3] == 'IOI':
        b += 1
print(a)
print(b)