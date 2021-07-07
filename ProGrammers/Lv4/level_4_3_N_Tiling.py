def solution(n):
    dp = [0 for _ in range(n + 1)]
    if n % 2 != 0:
        return 0
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3
        for j in range(0, i - 3, 2):
            dp[i] += (dp[j] * 2)
        dp[i] %= 1000000007
    return dp[n]

print(solution(4)) # 11

def solution(n):
    answer = 0
    prev = 3
    cur = 11
    if n == 2:
        return prev
    elif n == 4:
        return cur
    else:
        i = 6
        while i <= n:
            answer = 3*cur + (cur-prev)
            prev = cur
            cur = answer
            i += 2
    return answer % 1000000007

print(solution(4)) # 11