n = int(input())
a = sorted(map(int,input().split()))
b = list(map(int,input().split()))
answer = 0
for i in range(n):
    x, y = a[i], max(b)
    answer += x*y
    b.remove(y)
print(answer)

# ==========================================================
n = int(input())
a = sorted(map(int,input().split()))
b = sorted(map(int,input().split()), reverse=True)
answer = 0
for x, y in zip(a, b):
    answer += x*y
print(answer)