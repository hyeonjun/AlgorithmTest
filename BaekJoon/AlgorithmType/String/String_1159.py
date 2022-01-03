n = int(input())
name = {}
for _ in range(n):
    data = input()[0]
    if data not in name:
        name[data] = 1
    else:
        name[data] += 1
answer = []
for k in name.keys():
    if name[k] >= 5:
        answer.append(k)
if not answer:
    print("PREDAJA")
else:
    print(''.join(sorted(answer)))