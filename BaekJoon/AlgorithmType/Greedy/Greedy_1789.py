n = int(input())
answer, result = 0, 0
for i in range(1, n+1):
    if result+i <= n:
        result += i
        answer += 1
    else:
        break
print(answer)

# =================================

s = int(input())
n = 1
while n * (n+1) / 2 <= s:
    n += 1
print(n-1)