A, B = input().split()
x, y = 0, 0
for i in range(len(A)):
    if A[i] in B:
        x, y = B.index(A[i]), i
        break
for i in range(len(B)):
    if i == x:
        print(A)
    else:
        print('.' * y + B[i] + '.' * (len(A) - y -1))