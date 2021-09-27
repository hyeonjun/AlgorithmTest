t_c = int(input())
for _ in range(t_c):
    h, w, n = map(int, input().split())
    floor = n % h
    number = n //h +1
    if floor == 0:
        floor, number = h, n//h
    print(floor * 100 + number)

"""
6층 12호실까지
10번째 - 402호
10 % 6 = 4 -> 4번째 -> 4층
10 // 6 = 1 -> 1호실꽉참 -> 2호실

6층 12호실
12번째 - 602호
12 % 6 = 0 -> 젤 위
12 // 6 = 2 -> 마지막 2호실

"""