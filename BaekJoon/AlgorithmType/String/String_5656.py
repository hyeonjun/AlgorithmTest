idx = 1
while True:
    exp = list(input().split())
    if exp[1] == 'E':
        break
    flag = eval(''.join(exp))
    print(f'Case {idx}: {str(flag).lower()}')
    idx += 1