n = input()
m = input()

stack = []
for i in n:
    stack.append(i)
    if i == m[-1] and ''.join(stack[-len(m):]) == m:
        del stack[-len(m):]

print("".join(stack) if len(stack) > 0 else "FRULA")
