a, b, c = map(int, input().split())
time, maxtime = [], 0
for _ in range(3):
    s, e = map(int, input().split())
    time.append([s, e])
    maxtime = max(maxtime, e)
parking = [0 for _ in range(maxtime)]
for t in time:
    for i in range(t[0], t[1]):
        parking[i] += 1
answer = 0
for i in parking:
    if i == 1:
        answer += a
    if i == 2:
        answer += b * 2
    if i == 3:
        answer += c * 3
print(answer)


