k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start, end = 1, max(lan) # 랜선 길이 기준
while start <= end:
    mid = (start + end) // 2
    line = 0 # 랜선 수
    for l in lan:
        line += l // mid
    if n <= line:
        start = mid+1
    else:
        end = mid-1
print(end)

"""
4 11
802
743
457
539
=> 200
"""