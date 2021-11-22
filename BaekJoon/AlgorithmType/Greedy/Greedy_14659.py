n = int(input())
height = list(map(int, input().split()))
answer = [0 for _ in range(n)]
for i in range(n):
    cnt = 0
    for j in range(i+1, n):
        if height[i] > height[j]:
            cnt += 1
        else:
            break
    answer[i] = cnt
print(max(answer))