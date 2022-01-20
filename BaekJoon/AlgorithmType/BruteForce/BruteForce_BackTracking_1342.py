string = input()
cnt = [0 for _ in range(26)]
for s in string:
    cnt[ord(s) - ord('a')] += 1
answer = 0
def dfs(idx):
    global answer
    if sum(cnt) == 0:
        answer += 1
        return
    for i in range(26):
        if cnt[i] > 0 and idx != i: # 중복없애기
            cnt[i] -= 1
            dfs(i)
            cnt[i] += 1
dfs(-1)
print(answer)