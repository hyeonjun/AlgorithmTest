k, a, b = map(int, input().split())
answer = 0
if (a > 0 and b > 0) or (a < 0 and b < 0): # 0 포함 X
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
    answer += b//k - a//k
    if a % k == 0:
        answer += 1
else: # 0 포함
    answer += abs(a)//k + b//k + 1
print(answer)