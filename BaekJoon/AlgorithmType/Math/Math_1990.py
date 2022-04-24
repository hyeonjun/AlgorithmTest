a, b = map(int, input().split())
if b > 10000000: # 10,000,000보다 큰 숫자에는 팰린드롬 소수가 없음
    b = 10000000
prime = [True for _ in range(b+1)]
for i in range(2, int(b ** 0.5) +1):
    if prime[i]:
        for j in range(i*2, b+1, i):
            if prime[j]:
                prime[j] = False

def palindrome(x):
    return x == x[::-1]

for i in range(a, b+1):
    if prime[i] and palindrome(str(i)):
        print(i)
print(-1)