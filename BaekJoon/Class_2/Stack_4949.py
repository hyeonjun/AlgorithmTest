while True:
    data = input()
    if data == '.':
        break
    bracket = []
    flag = True
    for i in data:
        if i == '[' or i == '(':
            bracket.append(i)
        elif i == ']' or i == ')':
            if len(bracket) == 0:
                flag = False
                break
            x = bracket.pop()
            if (i == ']' and x != '[') or (i == ')' and x != '('):
                flag = False
    print('yes') if flag and not bracket else print('no')