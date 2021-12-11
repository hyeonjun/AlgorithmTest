n, m = map(int, input().split())
arr = [0 for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    newArr = [k for _ in range(j-i+1)]
    arr[i-1:j] = newArr
print(*arr)