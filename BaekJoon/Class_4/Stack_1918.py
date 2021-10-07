exp = input() # A*(B+C) -> ABC+* | (A+(B*C))-(D/E) -> ABC*+DE/-
stack = []
result = ''
for i in exp:
    if i.isalpha(): # 피연산자
        result+=i
    else:
        if i == "(":
            stack.append(i)
        elif i == "*" or i == "/":
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop() # '(' 제거
while stack:
    result += stack.pop()
print(result)