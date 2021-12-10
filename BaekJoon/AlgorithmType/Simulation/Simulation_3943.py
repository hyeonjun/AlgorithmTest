import sys
input = sys.stdin.readline
def recursive(n, maxV):
    if maxV < n:
        maxV = n
    if n == 1:
        return maxV
    if n % 2 == 0:
        return recursive(n // 2, maxV)
    else:
        return recursive(n * 3 + 1, maxV)
for _ in range(int(input())):
    n = int(input())
    print(recursive(n, n))