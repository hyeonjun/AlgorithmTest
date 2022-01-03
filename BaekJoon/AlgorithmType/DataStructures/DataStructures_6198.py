n = int(input())
arr = list(int(input()) for _ in range(n))
stack = []
answer = 0
for a in arr:
    while stack and stack[-1] <= a:
        stack.pop()
    stack.append(a)
    answer += len(stack)-1
print(answer)