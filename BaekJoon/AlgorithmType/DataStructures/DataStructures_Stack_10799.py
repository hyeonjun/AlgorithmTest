bracket = input()
answer = 0
stack = []
for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append('(')
    else: # ')'
        if bracket[i-1] == '(': # 레이저
            answer += len(stack)-1 # 레이저일때는 막대 새로 안생김
        else: # ')' => 막대 끝
            answer += 1
        stack.pop()
print(answer)