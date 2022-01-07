n = int(input())
V = input()
a, b = 0, 0
for v in V:
    if v == 'A':
        a += 1
    else:
        b += 1
print('Tie' if a == b else 'A' if a > b else 'B')