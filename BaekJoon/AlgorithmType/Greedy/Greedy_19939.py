n, k = map(int, input().split())
b = k * (k+1) // 2
if b > n:
    print(-1)
elif (n-b) % k == 0:
    print(k-1)
else:
    print(k)