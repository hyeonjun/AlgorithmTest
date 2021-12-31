answer = 0
for _ in range(int(input())):
    word = input()
    stack = []
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    if not stack:
        answer += 1
print(answer)