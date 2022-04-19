n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[0], x[1]))
answer = 0
for x, y in arr:
    if answer < x:
        answer = x
    answer += y
print(answer)