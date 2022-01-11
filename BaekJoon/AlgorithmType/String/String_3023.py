r, c = map(int, input().split())
arr = []
for _ in range(r):
    tmp = input()
    arr.append(list(tmp+tmp[::-1]))

for i in range(r-1, -1, -1):
    arr.append(arr[i][:])

a, b = map(int, input().split())
if arr[a-1][b-1] == '#':
    arr[a-1][b-1] = '.'
else:
    arr[a-1][b-1] = '#'

for i in arr:
    print(''.join(i))