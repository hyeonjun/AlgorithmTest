while True:
    A = list(input().lower())
    if A[0] == '#':
        break
    print(f'{A[0]} {A.count(A[0])-1}')