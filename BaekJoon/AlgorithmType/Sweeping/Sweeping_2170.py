import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
s, e = arr[0][0], arr[0][1]
answer = 0
for x, y in arr[1:]:
    if e > x:
        if e > y:
            continue
        else:
            e = y
    else:
        answer += e - s
        s, e = x, y
print(answer + (e-s))