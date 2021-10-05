import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dictionay = {}
for _ in range(n):
    site, pwd = input().strip().split()
    dictionay[site] = pwd

for _ in range(m):
    site = input().strip()
    print(dictionay[site])