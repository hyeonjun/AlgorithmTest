while True:
    string = input()
    if string == '*':
        break
    alpha = [0 for _ in range(26)]
    for s in string:
        if s == ' ':
            continue
        alpha[ord(s)-ord('a')] += 1
    flag = True
    for a in alpha:
        if a == 0:
            flag = False
    print('Y' if flag else 'N')