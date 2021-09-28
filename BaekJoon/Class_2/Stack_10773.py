k = int(input())
stack = []
for _ in range(k):
    x = int(input())
    if x != 0:
        stack.append(x)
    else:
        stack.pop()
    pass
print(sum(stack))
