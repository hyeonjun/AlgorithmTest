n, k = map(int, input().split())
answer = 0
while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1') # 1이상 존재하는 최소 물의 양
    n += 2**idx
    answer += 2**idx
print(answer)