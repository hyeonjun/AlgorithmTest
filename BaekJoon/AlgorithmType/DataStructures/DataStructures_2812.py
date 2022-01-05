n, k = map(int, input().split())
num = list(map(int, input()))
remove, stack = k, []
for i in range(n):
    while remove and stack and int(stack[-1]) < num[i]:
        stack.pop()
        remove -= 1
    stack.append(str(num[i]))
print(''.join(stack[:n-k]))