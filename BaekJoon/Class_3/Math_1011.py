import sys
t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    dis = y-x
    cnt = 0 # 이동 횟수
    move = 1 # 최대 이동 가능 거리
    sum_ = 0
    while sum_ < dis:
        cnt += 1
        sum_ += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)


"""
이동할 수 있는 거리 => k-1, k(이전에 움직인 거리) k+1
처음과 마지막은 1
거리      이동      횟수
1         1         1 -> 1
2        11         2 -> 1
3        111        3 -> 2 (4 - 1
4        121        3 -> 2
5        1211       4 -> 2
6        1221       4 -> 2 
7        12211      5 -> 3
8        12221      5 -> 3
9        12321      5 -> 3
10       123211     6 -> 3
11       123221     6 -> 3
12       123321     6 -> 3
13       1233211    7 -> 4
"""