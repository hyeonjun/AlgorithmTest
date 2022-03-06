n, x = map(int, input().split())
arr = list(map(int, input().split()))

if not sum(arr):
    print("SAD")
    exit()

ps = [0 for _ in range(n+1)]
for i in range(1, len(ps)):
    ps[i] += ps[i-1] + arr[i-1]

ansV, ansC = 0, 0
for i in range(x, len(ps)):
    value = ps[i]-ps[i-x]
    if ansV < value:
        ansV = value
        ansC = 1
    elif ansV == value:
        ansC += 1

print(ansV)
print(ansC)
