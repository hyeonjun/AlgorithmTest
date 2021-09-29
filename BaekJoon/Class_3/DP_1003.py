t = int(input())
for _ in range(t):
    n = int(input())
    fibo = [[1, 0], [0, 1]]
    for i in range(2, n+1):
        fibo.append([fibo[i-2][0]+fibo[i-1][0], fibo[i-2][1]+fibo[i-1][1]])
    print(fibo[n][0], fibo[n][1])
"""
0
1 0
1
0 1
2
1 1
3
1 2
4
2 3
5
3 5
"""