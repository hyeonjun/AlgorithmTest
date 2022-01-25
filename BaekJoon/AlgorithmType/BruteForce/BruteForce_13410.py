# 13410
n, k = map(int, input().split())
arr = [int(str(n*i)[::-1]) for i in range(1, k+1)]
print(max(arr))

# 17173
n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(1, n+1):
    for a in arr:
        if i % a == 0:
            answer += i
            break
print(answer)

# 2659
def solv(x):
    tmp = x
    for i in range(3):
        x = x % 1000 * 10 + x // 1000
        tmp = min(tmp, x)
    return tmp

arr = input().split()
res = solv(int(''.join(arr)))
answer = 0
for i in range(1111, res+1):
    if solv(i) == i:
        answer += 1
print(answer)