string = input()
stack = []
n = len(string)
for i in range(n):
    if i < n-1 and string[i+1] == '(': # 반복해야할 횟수
        stack.append(int(string[i]))
    elif string[i] == '(':
        stack.append(string[i])
    elif string[i] == ')':
        cnt = 0
        while True:
            tmp = stack.pop()
            if tmp == '(':
                break
            cnt += tmp
        stack.append(stack.pop() * cnt)
    else:
        stack.append(1) # 길이
print(sum(stack))