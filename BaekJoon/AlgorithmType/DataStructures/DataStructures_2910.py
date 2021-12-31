n, c = map(int, input().split())
arr = list(map(int, input().split()))
num = {}
for i in arr:
    if i not in num:
        num[i] = 1
    else:
        num[i] += 1
num = sorted(num.items(), key=lambda x:(-x[1]))
answer = []
for v, i in num:
    answer.extend([v] * i)
print(*answer)