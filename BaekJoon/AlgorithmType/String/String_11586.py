n = int(input())
arr = [input() for _ in range(n)]
idx = int(input())
if idx == 1:
    for a in arr:
        print(a)
if idx == 2:
    answer = [[] for _ in range(n)]
    for j in range(n-1, -1, -1):
        for i in range(n):
            answer[i].append(arr[i][j])
    for a in answer:
        print(''.join(a))
if idx == 3:
    for i in range(n-1, -1, -1):
        print(arr[i])