# 100점
n = int(input())
m = int(input())
S = input()

ans = 0
p = 0
i = 1
while i < m-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        p += 1
        if p == n:
            p -= 1
            ans += 1
        i += 1
    else:
        p = 0
    i += 1
print(ans)

# 50점
P = 'I'
Pn = 'OI'
n = int(input())
m = int(input())
S = input()

P = P + Pn * n
idx = len(P)
cnt = 0
while idx < m:
    data = S[idx-len(P):idx]
    if P == data:
        cnt += 1
        idx += 2
    else:
        idx += 1
print(cnt)