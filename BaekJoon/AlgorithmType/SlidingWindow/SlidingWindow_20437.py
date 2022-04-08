from collections import Counter, defaultdict
for _ in range(int(input())):
    string = input()
    k = int(input())

    cnt = Counter(string)
    idx = defaultdict(list)
    for i in range(len(string)):
        if cnt[string[i]] >= k:
            idx[string[i]].append(i)

    if not idx:
        print(-1)
    else:
        ans1, ans2 = float('inf'), -1
        for i in idx.values():
            for j in range(len(i)-k+1):
                length = i[j+k-1] - i[j] + 1
                ans1 = min(ans1, length)
                ans2 = max(ans2, length)
        print(ans1, ans2)