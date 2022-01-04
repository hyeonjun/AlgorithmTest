for _ in range(int(input())):
    A, B = input().split('-')
    a = sum([ (ord(A[i])-ord('A')) * 26 ** (2-i) for i in range(len(A))])
    if abs(a - int(B)) <= 100:
        print('nice')
    else:
        print('not nice')