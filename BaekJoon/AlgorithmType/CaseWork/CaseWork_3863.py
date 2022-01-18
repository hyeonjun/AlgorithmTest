while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    arr1 = []
    for _ in range(n):
        _, _, start, duration = map(int, input().split())
        arr1.append([start, start+duration])
    arr2 = []
    for _ in range(m):
        s, d = map(int, input().split())
        arr2.append([s, s+d])
    answer = [0 for _ in range(m)]
    for x in range(m):
        i, j = arr2[x]
        for k, l in arr1:
            # if (i <= k and k < j) or (k <= i and j <= l) or (i < l and l <= j):
            if l > i and k < j:
                answer[x] += 1
    for a in answer:
        print(a)