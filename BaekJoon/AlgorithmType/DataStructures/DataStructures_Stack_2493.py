n = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0 for _ in range(n)]
for i in range(n):
    while stack and top[stack[-1]] < top[i]:
        stack.pop() # 현재 탑의 높이보다 작은 탑은 없앰
    if stack:
        answer[i] = stack[-1]+1
    stack.append(i)
print(*answer)