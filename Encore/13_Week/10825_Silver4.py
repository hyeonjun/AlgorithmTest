for a in sorted([input().split() for _ in range(int(input()))], key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    print(a[0])