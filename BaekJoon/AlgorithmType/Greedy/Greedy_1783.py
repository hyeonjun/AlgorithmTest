n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2: # 2번 3번 행동만 가능
    print(min(4, (m+1)//2))
else:
    if m <= 6: # 세로 3이상 가로 6이하,
        print(min(4, m))
    else:
        print(m-2)