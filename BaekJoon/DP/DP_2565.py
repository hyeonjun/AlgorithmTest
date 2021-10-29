"""
a전봇대나 b전봇대 기준으로 정렬시킨다
a전봇대 기준으로 정렬시키면
1  8
2  2
3  9
4  1
6  4
7  6
9  7
10 10
이 되는데 여기서 b전봇대의 가장 긴 증가하는 부분수열을 구하면
(4,1) (6,4) (7,6) (9,7) (10,10)이 된다. 이 부분은 교차하지 않는다.
즉 8-5를 하면 제거해야할 전깃줄 수가 나온다.
"""
n = int(input())
wire = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x:x[0])
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if wire[j][1] < wire[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))
