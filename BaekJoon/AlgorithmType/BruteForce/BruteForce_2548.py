n = int(input())
arr = list(map(int, input().split()))

# 중앙값
arr.sort()
if len(arr) % 2 == 0:
    print(arr[len(arr) // 2 -1])
else:
    print(arr[len(arr) // 2])

# 브루트포스
answer = 0
sub = 1e9
for i in arr:
    tmp = 0
    for j in arr:
        tmp += abs(i-j)
    if sub > tmp:
        sub = tmp
        answer = i
    if sub == tmp and answer > i:
        answer = i
print(answer)