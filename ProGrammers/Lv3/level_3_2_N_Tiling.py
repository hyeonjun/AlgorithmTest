def solution(n):
    import sys
    sys.setrecursionlimit(60000) # 재귀 호출 제한을 품

    # 가로 길이 1 => 1개
    # 가로 길이 2 => 2개
    # 가로 길이 3 => 가로길이 1 + 가로길이 2
    # 점화식 : DP(n) = DP(n-1) + DP(n-2)

    mem = [-1] * 60001 # 가로 최대 길이는 60000
    def dp(n):
        if mem[n] != -1:
            return mem[n]
        if n == 0:
            return 1
        if n == 1:
            return 1
        mem[n] = (dp(n-1) + dp(n-2)) % 1000000007
        return mem[n]
    return dp(n)

print(solution(4)) # 5

def solution(n):
    a, b = 1, 1
    for i in range(n):
        a,b = b, a+b
    return a % 1000000007

print(solution(4)) # 5
