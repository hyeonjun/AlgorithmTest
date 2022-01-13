import math
n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
answer = 0
plankIdx = 0
for s, e in arr:
    if s <= plankIdx:
        s = plankIdx +1
        if e <= s:
            continue
    curPlank = math.ceil((e-s)/l)
    answer += curPlank
    plankIdx = max(plankIdx, s + curPlank*l - 1)
print(answer)