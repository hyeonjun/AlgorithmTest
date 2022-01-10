n = int(input())
answer = list(input())
for _ in range(n-1):
    tmp = list(input())
    for i in range(len(answer)):
        if answer[i] != tmp[i]:
            answer[i] = '?'
print(''.join(answer))
