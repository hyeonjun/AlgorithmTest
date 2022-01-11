n = int(input())
arr = list(map(int, input().split()))
count = {}
for i in arr:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

answer = [-1 for _ in range(n)]
stack = []

for i in range(n):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)