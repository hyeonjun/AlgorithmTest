def solution(n):
    fibo = [0, 1, 2]
    for i in range(2, n):
        fibo.append((fibo[i] + fibo[i-1]) % 1234567)
    return fibo[n]

print(solution(4)) # 5
print(solution(3)) # 3