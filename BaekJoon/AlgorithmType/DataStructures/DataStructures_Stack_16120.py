ppap = input()
if ppap == 'P' or ppap == 'PPAP':
    print("PPAP")
else:
    stack = []
    for s in ppap:
        stack.append(s)
        if ''.join(stack[-4:]) == 'PPAP':
            stack.pop(); stack.pop(); stack.pop(); # P만 남김
    stack = ''.join(stack)
    if stack == 'P' or stack == 'PPAP':
        print('PPAP')
    else:
        print('NP')
