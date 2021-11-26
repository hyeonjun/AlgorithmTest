n, k = map(int, input().split())
hp = list(input())
answer = 0
for i in range(n):
    if hp[i] == 'P':
        for j in range(i-k, i+k+1):
            if j > -1 and j < n and hp[j] == 'H':
                hp[j] = '.'
                answer += 1
                break
print(answer)