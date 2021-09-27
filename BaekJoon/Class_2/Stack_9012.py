n = int(input())
for _ in range(n):
    data = input()
    stack = []
    flag = True
    for d in data:
        if d == '(':
            stack.append(d)
        else:
            if not stack:
                flag = False
                break
            stack.pop()
    print("YES") if flag and not stack else print("NO")