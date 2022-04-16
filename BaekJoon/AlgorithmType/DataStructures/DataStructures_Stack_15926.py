n = int(input())
basket = input()

stack = []
check = [0 for _ in range(n)]
for i in range(len(basket)):
    if basket[i] == '(':
        stack.append(i)
    else:
        if stack:
            check[i] = check[stack.pop()] = 1
answer, tmp = 0, 0
for c in check:
    if c:
        tmp += 1
        answer = max(answer, tmp)
    else:
        tmp = 0
print(answer)