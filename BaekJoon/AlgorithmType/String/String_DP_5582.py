"""
A = 'BACDEA'
B = 'ABCACDEC'
    A B C A C D E C
  0 0 0 0 0 0 0 0 0
B 0 0 1 0 0 0 0 0 0
A 0 1 0 0 1 0 0 0 0
C 0 0 0 1 0 2 0 0 1
D 0 0 0 0 0 0 3 0 0
E 0 0 0 0 0 0 0 4 0
A 0 1 0 0 1 0 0 0 0
 -> 답 : 4
if A[i] == B[j]:
    dp[i][j] = dp[i-1][j-1] + 1
"""

A = input()
B = input()
dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
answer = 0
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])
print(answer)