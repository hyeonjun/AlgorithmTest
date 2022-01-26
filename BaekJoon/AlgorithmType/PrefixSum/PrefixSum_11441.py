import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix[i] = arr[i-1] + prefix[i-1]


for _ in range(int(input())):
    i, j = map(int, input().split())
    print(prefix[j]-prefix[i-1])