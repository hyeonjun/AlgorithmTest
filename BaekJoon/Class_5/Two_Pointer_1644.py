n = int(input())

# 에라토스테네스의 체
prime_check = [True for _ in range(n+1)]
prime_num = []
for i in range(2, int(n ** 0.5)+1):
    if prime_check[i]:
        for j in range(i+i, n+1, i):
            prime_check[j] = False

for i in range(2,n+1):
    if prime_check[i]:
        prime_num.append(i)

cnt = 0
left, right = 0, 1

while right <= len(prime_num):
    sumV = sum(prime_num[left:right])
    if sumV == n:
        cnt += 1
        right += 1
    elif sumV < n:
        right += 1
    else:
        left += 1
print(cnt)
