n = int(input())
arr = list(map(int, input().split()))
x, y = arr[0], sorted(arr[1:])
flag = True
for i in y:
    if x > i:
        x += i
    else:
        flag = False
print("Yes" if flag else "No")