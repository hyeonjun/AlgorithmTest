def factorial(N,T,L):
    fac = 1
    for i in range(1,N+1):
        fac *= i
        if fac * T > L:
            return True
    return False

for _ in range(int(input())):
    D = input().split()
    S = D[0]
    N, T, L = map(int, D[1:])
    L *= 10 ** 8
    answer = True
    if S == 'O(N)' and L < N * T:
        answer = False
    elif S == 'O(N^2)' and L < N **2 * T:
        answer = False
    elif S == 'O(N^3)' and L < N **3 * T:
        answer = False
    elif S == 'O(2^N)' and L < 2 ** N * T:
        answer = False
    elif S == 'O(N!)' and factorial(N, T, L):
        answer = False
    print('May Pass.' if answer else 'TLE!')
