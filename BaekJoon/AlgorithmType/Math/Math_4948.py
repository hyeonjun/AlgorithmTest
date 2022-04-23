# 에라토스테네스의 체
prime = [True for _ in range(246912+1)]
for i in range(2, int(246912 ** 0.5)+1):
    if prime[i]:
        for j in range(i*2, 246912+1, i):
            prime[j] = False

while True:
    x = int(input())
    if not x:
        break
    answer = 0
    for i in range(x+1, 2*x+1):
        if prime[i]:
            answer += 1
    print(answer)