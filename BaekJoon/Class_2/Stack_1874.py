n = int(input())
stack = []
result = []
y = 0
flag = True

for i in range(n):
    x = int(input())
    while y < x:
        y += 1
        stack.append(y)
        result.append('+')
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        flag = False
print('\n'.join(result)) if flag else print('NO')

"""
8
4
3
6
8
7
5
2
1
=> + + + + - - + + - + + - - - - -
 
5
1
2
5
3
4
=> NO

"""
