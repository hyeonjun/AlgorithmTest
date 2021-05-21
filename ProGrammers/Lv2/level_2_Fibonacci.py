def solution_1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % 1234567

def solution_2(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        data = fibo[i-2] + fibo[i-1]
        fibo.append(data)
    return fibo[-1] % 1234567

data = [3, 5] # 2 5
for i in data:
    print(solution_1(i))
    print(solution_2(i))

