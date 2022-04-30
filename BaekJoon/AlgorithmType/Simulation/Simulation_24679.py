import sys
input = sys.stdin.readline
for _ in range(int(input())):
    arr = sorted(map(int, input().split()))
    if arr[0] == 1:
        if arr[1] == arr[2] and arr[1] % 2:
            print("B")
        else:
            print("R")
    else:
        w = min(arr[2], arr[0] + arr[1] - 2)
        if (all(not i % 2 for i in arr[:2]) and not w % 2) or  (arr[0] + arr[1] + w) % 4 == 3:
            print("B")
        else:
            print("R")