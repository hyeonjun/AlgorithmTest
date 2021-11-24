n = int(input())
tip = [int(input()) for _ in range(n)]
tip.sort(reverse=True)
answer = 0
for i in range(n):
    t = tip[i]-i
    answer += t if t > 0 else 0
print(answer)