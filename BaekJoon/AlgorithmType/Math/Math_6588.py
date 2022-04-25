prime = [True for _ in range(1000001)]
for i in range(2, int(1000000 ** 0.5)+1):
    if prime[i]:
        for j in range(i*2, 1000001, i):
            if prime[j]:
                prime[j] = False

while True:
    n = int(input())
    if n == 0: break
    for i in range(3, n//2+1, 2):
        if prime[i] and prime[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
