for _ in range(int(input())):
    m,n,x,y = map(int, input().split())
    # n, m의 최소 공배수가 마자막 해.
    while x <= m * n:
        # if x % n == y % n:
        if (x - y) % n == 0:
            print(x)
            break
        x += m # (x + m) % m == x % m
    else:
        print(-1)

"""
<m, n> == <10, 12>
1번째 해 => <1, 1>
2번쩨 해 => <2, 2>
3번쩨 해 => <3, 3>
...
12번쩨 해 => <2, 12>
13번쩨 해 => <3, 1>
...

29 9 5
30 10 6
31 1 7
32 2 8
33 3 9
34 4 10
"""