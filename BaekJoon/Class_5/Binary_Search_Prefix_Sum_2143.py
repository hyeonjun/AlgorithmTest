from collections import defaultdict
t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

cnt = 0
prefix_A = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        prefix_A[sum(A[i:j+1])] += 1
print(prefix_A)
for i in range(m):
    for j in range(i, m):
        cnt += prefix_A[t - sum(B[i:j+1])] # t에서 B 부분합을 빼서 나온 값이 A 부분합에 있으면 가능
print(cnt)