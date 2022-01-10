n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1 for _ in range(n)]
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]: # 스택에 있는 위치의 값보다 큰 값이 나오면
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)