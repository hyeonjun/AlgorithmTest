n = int(input())
antenna = sorted(map(int, input().split()))
print(antenna[(n-1)//2])