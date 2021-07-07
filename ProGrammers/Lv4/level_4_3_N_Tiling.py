# n이 홀수일 때는 주어진 타일로는 채울 수 있는 방법이 없다
# if n == 2 -> 3
# if n == 4 -> (2,2) = 3*3 = 9 + (4) -> 2 = 11
"""
f(4) = 3f(2) + 2
f(6) = 3f(4) + 2f(2) + 2
f(8) = 3f(6) + 2f(4) + 2f(2) + 2
...
f(n) = 3f(n-2) + 2f(n-4) + 2f(n-6) + ... + 2f(2) + 2
"""
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