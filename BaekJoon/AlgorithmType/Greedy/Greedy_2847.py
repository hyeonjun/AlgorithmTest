n = int(input())
score = [int(input()) for _ in range(n)]
answer = 0
for i in range(n-2, -1, -1):
    if score[i] >= score[i+1]:
        d = score[i] - (score[i+1]-1)
        answer += d
        score[i] -= d
print(answer)