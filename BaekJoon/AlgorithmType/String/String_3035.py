r, c, zr, zc = map(int, input().split())
arr = [input() for _ in range(r)]
answer = []
for i in arr:
    tmp = ''
    for j in i:
        tmp += j * zc
    for _ in range(zr):
        answer.append(tmp)
for a in answer:
    print(a)