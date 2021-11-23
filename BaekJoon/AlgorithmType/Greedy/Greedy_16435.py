n, l = map(int, input().split())
H = sorted(map(int, input().split()))
for h in H:
    if l >= h:
        l += 1
    else:
        break
print(l)