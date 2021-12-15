for _ in range(int(input())):
    n, m = map(int, input().split())
    answer = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            data = a**2 + b**2 + m
            r = a * b
            if data // r == data / r:
                answer += 1
    print(answer)