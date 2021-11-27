n = int(input())
k = int(input())
sensor = sorted(map(int, input().split()))
if k >= n:
    print(0)
else:
    distance = []
    for i in range(1, n):
        distance.append(sensor[i] - sensor[i-1])
    distance.sort(reverse=True)
    for _ in range(k-1):
        distance.pop(0)
    print(sum(distance))