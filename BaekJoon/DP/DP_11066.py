"""
40 30 30 50
0 40 70 100 150
길이 2
   0    1   2   3   4
0  0    0   0   0   0
1  0    0  70   0   0
2  0    0   0  60   0
3  0    0   0   0  80
4  0    0   0   0   0
1~2 : 0(1~1) + 0(2~2) + 70(누적합([2]-[0])) = 70
2~3 : 0(2~2) + 0(3~3) + 60(누적합([3]-[1])) = 60
3~4 : 0(3~3) + 0(4~4) + 80(누적합([4]-[2])) = 80

길이 3
   0    1   2   3   4
0  0    0   0   0   0
1  0    0  70 160   0
2  0    0   0  60 170
3  0    0   0   0  80
4  0    0   0   0   0
1~3 : min(70(1~2)+0(3), 0(1)+60(2~3)) + 100(누적합([3]-[0])) = 160
2~4 : min(60(2~3)+0(4), 0(2)+60(3~4)) + 110(누적합([4]-[1])) = 170

길이 4
   0    1   2   3   4
0  0    0   0   0   0
1  0    0  70 160 300
2  0    0   0  60 170
3  0    0   0   0  80
4  0    0   0   0   0
1~4 : min(170(1+(2~4)), 150((1~2)+(3~4)), 160((1~3)+4)) + 150누적합([4]-[0]) = 300

i:start, k:mid, j:end
dp[i][j] = dp[i][k] + dp[k+1][j] + sum(list[i]~list[j])
"""
for _ in range(int(input())):
    n = int(input())
    file = list(map(int, input().split()))
    prefix_sum = [0]
    for i in file:
        prefix_sum.append(prefix_sum[-1]+i)

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for j in range(2, n+1):
        for i in range(1, n+2-j):
            dp[i][i+j-1] = min([dp[i][i+k]+dp[i+k+1][i+j-1] for k in range(j-1)]) + (prefix_sum[i+j-1] - prefix_sum[i-1])
    print(dp[1][-1])







