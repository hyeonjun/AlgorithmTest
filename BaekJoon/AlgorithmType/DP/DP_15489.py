arr = [[1]]
for i in range(29):
    tmp = [1] + [arr[-1][j] + arr[-1][j+1] for j in range(i)] + [1]
    arr.append(tmp)

r, c, w = map(int, input().split())
answer = 0
for i in range(r, r+w):
    for j in range(c, c+(i-r)+1):
        answer += arr[i-1][j-1]
print(answer)