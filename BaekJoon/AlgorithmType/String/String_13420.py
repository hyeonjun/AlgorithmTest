for _ in range(int(input())):
    exp = input().split()
    if eval(''.join(exp[:-2])) == int(exp[-1]):
        print('correct')
    else:
        print('wrong answer')