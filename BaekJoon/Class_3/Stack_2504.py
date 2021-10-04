"""
(   (
(   ((
)   (2
[   (2[
[   (2[[
"""
import sys
input = sys.stdin.readline().rstrip()
stack = []

for i in input:
    if i == ")":
        if len(stack) > 0:
            tmp = 0
            while stack:
                x = stack.pop()
                if x == '(':
                    stack.append(2 if tmp == 0 else tmp * 2)
                    break
                elif x == '[':
                    print(0)
                    exit(0)
                else:
                    tmp += x
        else:
            print(0)
            exit(0)
    elif i == "]":
        if len(stack) > 0:
            tmp = 0
            while stack:
                x = stack.pop()
                if x == '[':
                    stack.append(3 if tmp == 0 else tmp * 3)
                    break
                elif x == '(':
                    print(0)
                    exit(0)
                else:
                    tmp += x
        else:
            print(0)
            exit(0)
    else:
        stack.append(i)
print(0 if '(' in stack or '[' in stack else sum(stack))

# (()[[]])([]) 28
# [][]((]) 0