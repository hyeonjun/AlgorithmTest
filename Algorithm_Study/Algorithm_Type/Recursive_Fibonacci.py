def solution(n):
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append(answer[i-2]+answer[i-1])
    return answer[-1]

print(solution(10))

def solution(n):
    answer = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        answer[i] = (answer[i-2]+answer[i-1])
    return answer[-1]

print(solution(10))

def solution(n):
    a,b = 0,1
    while n>0:
        a,b = b, a+b
        n-=1
    return a

print(solution(10))

def solution(n): # 오래 걸림
    def fibo(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibo(n-1) + fibo(n-2)
    return fibo(n)

print(solution(10)) # 55