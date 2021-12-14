h, w = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

for i in range(1, w-1):
    left, right = max(block[:i]), max(block[i+1:])
    m = min(left, right)
    if m > block[i]:
        answer += m - block[i]
print(answer)
