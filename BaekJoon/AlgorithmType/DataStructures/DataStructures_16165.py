n, m = map(int, input().split())
girlGroup = {}
for _ in range(n):
    group = input()
    num = int(input())
    name = []
    for _ in range(num):
        s = input()
        name.append(s)
    girlGroup[group] = sorted(name)
answer = []
for _ in range(m):
    name = input()
    types = int(input())
    if types == 0:
        answer.extend(girlGroup[name])
    else:
        for k in girlGroup.keys():
            if name in girlGroup[k]:
                answer.append(k)
                break
for a in answer:
    print(a)
