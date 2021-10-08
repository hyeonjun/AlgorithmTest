n = int(input())
maxdp = [0 for _ in range(6)]
mindp = [0 for _ in range(6)]

for _ in range(n):
    score = list(map(int, input().split()))

    maxdp[0] = max(maxdp[3], maxdp[4]) + score[0]
    maxdp[1] = max(maxdp[3], maxdp[4], maxdp[5]) + score[1]
    maxdp[2] = max(maxdp[4], maxdp[5]) + score[2]

    mindp[0] = min(mindp[3], mindp[4]) + score[0]
    mindp[1] = min(mindp[3], mindp[4], mindp[5]) + score[1]
    mindp[2] = min(mindp[4], mindp[5]) + score[2]

    for i in range(3):
        maxdp[i+3] = maxdp[i]
        mindp[i+3] = mindp[i]

print(max(maxdp[0], maxdp[1], maxdp[2]), min(mindp[0], mindp[1], mindp[2]))


"""
슬라이딩 윈도우
x) 피보나치 수열 -> n번째 수 구할때

fibo = [0 for _ in range(n)]
if n == 0:
    fibo[n] = 0
elif i == 1:
    fibo[n] = 1
else:
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
=> 공간복잡도 O(n)

fibo = [0, 0, 0]
if n == 0:
    fibo[n] = 0
elif n == 1:
    fibo[n] = 1
else:
    for i in range(2, n+1):
        fibo[i%3] = fibo[(i-1) % 3] + fibo[(i-1) % 3]
=> 슬라이딩 윈도우는 메모리 초과를 방지할 수 있다.
"""