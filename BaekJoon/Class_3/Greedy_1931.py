n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x:(x[1], x[0])) # 끝나는 시간으로 정렬 후, 시작시간으로 정렬


cnt = [1,1] # 0번째로 시작, 1번째로 시작
for i in range(2):
    current = time[i]
    for j in range(i+1, len(time)):
        if current[1] > time[j][0]:
            continue
        current = time[j]
        cnt[i] += 1
print(max(cnt))

# 정렬이 되어있어서 굳이 몇번째로 시작할건지 구하지 않아도 되는 듯.
cnt = 0
current = 0
for s, e in time:
    if s >= current:
        cnt += 1
        current = e
print(cnt)