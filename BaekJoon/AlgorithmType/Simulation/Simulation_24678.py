import sys
input = sys.stdin.readline
for _ in range(int(input())):
    arr = sorted(map(int, input().split()))
    if not arr[1]:
        print("R")
        continue
    arr = [i % 2 for i in arr]
    if not sum(arr):
        print("R")
    elif sum(arr) == len(arr):
        print("B")
    else:
        print("B" if not sum(arr) % 2 else "R")