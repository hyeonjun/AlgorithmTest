n = int(input())
exp = input()
value = {}
for i in range(n):
    value[chr(ord('A')+i)] = int(input())

stack = []
for e in exp:
    if e.isalpha():
        stack.append(value[e])
    else:
        n2, n1= stack.pop(), stack.pop()
        if e == '+':
            stack.append(n1+n2)
        elif e == '-':
            stack.append(n1-n2)
        elif e == '*':
            stack.append(n1*n2)
        elif e == '/':
            stack.append(n1/n2)
print('{0:.2f}'.format(stack[0]))