def solution(A):
    N = len(A)
    S = 0
    for i in range(N):
        A[i] = abs(A[i])
        S += A[i]
    M = max(A)

    count = [0] * (M+1)

    for i in range(N):
        count[A[i]] += 1

    dp = [-1] * (S + 1)
    dp[0] = 0

    for i in range(1, M+1):
        if count[i] > 0:
            for j in range(S):
                if dp[j] >= 0:
                    dp[j] = count[i]
                elif j>=i and dp[j-i] > 0:
                    dp[j] = dp[j-i]-1
    result = S
    for i in range(S//2 + 1):
        if dp[i] >= 0:
            result = min(result, S-2 * i)

    return result
print(solution([1,5,2,-2]))
# print(solution([-4,-2,5,6,7,-1,-2,3]))
# print(solution([3,3,3,4,5]))