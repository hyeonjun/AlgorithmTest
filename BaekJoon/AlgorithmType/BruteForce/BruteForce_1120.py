a, b = input().split()
answer = []
for i in range(len(b) - len(a) +1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    answer.append(cnt)
print(min(answer))