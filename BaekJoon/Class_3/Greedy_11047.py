n, k = map(int, input().split())
coin = sorted([int(input()) for _ in range(n)], reverse=True)
cnt = 0
while k > 0:
    for c in coin:
        if c <= k:
            q, r = divmod(k, c)
            cnt += q
            k = r
print(cnt)