# 잘 모르겠다..
a, b = map(int, input().split())

def cnt(n):
    if n == 0: return 0
    l = len(str(bin(n))[2:])
    high_one = n - 2**(l-1) + 1 # 최상위 1의 개수
    full_one = (l-1) * 2 ** (l-2) # n-1 자리 수까지의 1의 개수
    remain = cnt(n-2 ** (l-1)) # 남은 자리 수
    return int(high_one + full_one + remain)

print(cnt(b) - cnt(a-1))