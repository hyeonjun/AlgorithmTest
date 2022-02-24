import sys
input = sys.stdin.readline
maxV = 10 ** 9

def exec(command, num):
    stack = [num]
    for cmd in command:
        c = cmd.split()
        if c[0] == 'NUM':
            stack.append(int(c[1]))
        elif not stack:
            return "ERROR"
        elif c[0] == 'POP':
            stack.pop()
        elif c[0] == 'INV':
            stack[-1] *= -1
        elif c[0] == 'DUP':
            stack.append(stack[-1])
        elif len(stack) == 1:
            return "ERROR"
        elif c[0] == 'SWP':
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif c[0] == 'ADD':
            add = stack.pop() + stack.pop()
            if abs(add) > maxV:
                return "ERROR"
            stack.append(add)
        elif c[0] == 'SUB':
            sub = -stack.pop() + stack.pop()
            if abs(sub) > maxV:
                return "ERROR"
            stack.append(sub)
        elif c[0] == 'MUL':
            mul = stack.pop() * stack.pop()
            if abs(mul) > maxV:
                return "ERROR"
            stack.append(mul)
        elif c[0] == 'DIV':
            a, b = stack.pop(), stack.pop()
            if a == 0:
                return "ERROR"
            div = abs(b) // abs(a)
            if (a < 0 and b > 0) or (a > 0 and b < 0):
                div *= -1
            if abs(div) > maxV:
                return "ERROR"
            stack.append(div)
        elif c[0] == 'MOD':
            a, b = stack.pop(), stack.pop()
            if a == 0:
                return "ERROR"
            mod = abs(b) % abs(a)
            if mod > maxV:
                return "ERROR"
            if b < 0:
                mod *= -1
            stack.append(mod)
        else:
            return "ERROR"
    if len(stack) == 1:
        return stack[0]
    return "ERROR"

while True:
    command = []
    end = False
    while True:
        c = input().strip()
        if c == 'QUIT':
            end = True
            break
        if c == 'END':
            break
        command.append(c)
    if end: break

    for _ in range(int(input())):
        n = int(input())
        print(exec(command, n))
    print()
    input()
