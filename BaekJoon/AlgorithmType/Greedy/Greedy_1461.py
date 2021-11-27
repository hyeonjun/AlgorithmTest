n, m = map(int, input().split())
location = list(map(int, input().split()))
positive, negative = [], []
maxD = 0
for l in location:
    if l > 0:
        positive.append(l)
    else:
        negative.append(abs(l))
    maxD = max(maxD, abs(l))
positive.sort(reverse=True)
negative.sort(reverse=True)
answer = 0
for i in range(0, len(positive), m):
    if positive[i] != maxD:
        answer += positive[i] * 2
for i in range(0, len(negative), m):
    if negative[i] != maxD:
        answer += negative[i] * 2
print(answer+maxD)
