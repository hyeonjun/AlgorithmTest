P, K = map(int, input().split())
prime = [True for _ in range(K+1)]
for i in range(2, int(K**0.5)+1):
    if prime[i]:
        for j in range(i*2, K+1, i):
            prime[j] = False
flag, r = True, 0
for i in range(2, K):
    if prime[i] and P % i == 0:
        flag = False
        r = i
        break

print('GOOD' if flag else f'BAD {r}')