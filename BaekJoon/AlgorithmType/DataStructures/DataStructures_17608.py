# 스택
n = int(input())
stack = []
for _ in range(n):
    num = int(input())
    while True:
        if stack and stack[-1] <= num:
            stack.pop()
        else:
            break
    stack.append(num)
print(len(stack))