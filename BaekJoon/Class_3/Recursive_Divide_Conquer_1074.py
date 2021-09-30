import sys
n, r, c = map(int, sys.stdin.readline().split())
cnt = 0

while n > 1:
    size = 2 ** (n-1)  # 한 사분면의 크기
    
    if r < size and c < size: # 2 사분면
        pass
    elif r < size and c >= size: # 1 사분면
        cnt += size ** 2 * 1
        c -= size
    elif r >= size and c < size: # 3 사분면
        cnt += size ** 2 * 2
        r -= size
    elif r >= size and c >= size: # 4 사분면
        cnt += size ** 2 * 3
        r -= size
        c -= size
    n -= 1 # 해당 사분면으로 진입

print(cnt if r == 0 and c == 0 else cnt+1 if r == 0 and c == 1 else cnt+2 if r == 1 and c == 0 else cnt+3)
    
# 재귀로 풀경우 시간초과 or 메모리 초과 발생함.

# n > 1인 경우 배열을 크기가 2^(n-1) * 2^(n-1)로 4등분, 한 사분면의 크기
# Z의 순서 : 2 사분면 -> 1 사분면 -> 3 사분면 -> 4 사분면
# ex)size = 2
# 00 01 | 02 03
# 10 11 | 12 13
# ------+-------
# 20 21 | 22 23
# 30 31 | 32 33
# 2사분면 -> r < size, c < size
# 1사분면 -> r < size, c >= size
# 3사분면 -> r >= size, c < size
# 4사분면 -> r >= size, c >= size
# 이후 해당 사분면을 다시 사분면으로 나누어 계산
# 2사분면 -> r, c
# 1사분면 -> r, c -= size
# 3사분면 -> r -= size, c
# 4사분면 -> r -= size, c -= size
