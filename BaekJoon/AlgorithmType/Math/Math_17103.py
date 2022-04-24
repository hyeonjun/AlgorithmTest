prime = [True for _ in range(1000000+1)]
for i in range(2, int(1000000 ** 0.5)+1):
    if prime[i]:
        for j in range(i*2, 1000000+1, i):
            if prime[j]:
                prime[j] = False

for _ in range(int(input())):
    n = int(input())
    answer = 0
    for i in range(2, n//2+1):
        if prime[i] and prime[n-i]:
            answer += 1
    print(answer)
