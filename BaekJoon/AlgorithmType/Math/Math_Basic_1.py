# 2914
a, i = map(int, input().split())
print(a * (i-1) +1)

# 3003
answer = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
for i in range(6):
    answer[i] -= arr[i]
print(*answer)

# 3046
r1, s = map(int, input().split())
print(s*2 - r1)

# 5522
answer = 0
for _ in range(5):
    answer += int(input())
print(answer)

# 5554
answer = 0
for _ in range(4):
    answer += int(input())
print(answer // 60)
print(answer % 60)

# 8393
n = int(input())
for i in range(1, n):
    n += i
print(n)

# 10430
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

# 10757
a, b = map(int, input().split())
print(a+b)