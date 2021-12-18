n, m = map(int, input().split())
if n < 3:
    print(0)
else:
    answer = 0
    unmixed = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        unmixed[a].append(b)
        unmixed[b].append(a)

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j in unmixed[i]:
                continue
            for k in range(j+1, n+1):
                if k in unmixed[i] or k in unmixed[j]:
                    continue
                answer += 1
    print(answer)