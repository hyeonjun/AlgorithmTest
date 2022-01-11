n = int(input())
s = [input() for _ in range(n)]
cnt_w, cnt_h = 0, 0
answer = [0, 0]
for i in s:
    for j in i:
        if j == '.':
            cnt_w += 1
        else:
            if cnt_w > 1:
                answer[0] += 1
            cnt_w = 0
    if cnt_w > 1:
        answer[0] += 1
    cnt_w = 0
for i in range(n):
    for j in range(n):
        if s[j][i] == '.':
            cnt_h += 1
        else:
            if cnt_h > 1:
                answer[1] += 1
            cnt_h = 0
    if cnt_h > 1:
        answer[1] += 1
    cnt_h = 0
print(*answer)