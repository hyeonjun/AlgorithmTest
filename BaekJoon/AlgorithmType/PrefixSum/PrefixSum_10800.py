# 정렬을 했을 때 A, B가 있다면
# A가 잡을 수 있는 모든 컬러볼은 B도 잡을 수있다.
n = int(input())
arr = []
for i in range(n):
    c, s = map(int, input().split())
    arr.append((s, c, i))

arr.sort() # 크기 기준 정렬

prefix = [0 for _ in range(n+1)] # 컬러별 크기 합
total = 0 # 컬러 상관없이 현재 위치 컬러볼이 잡을 수 있는 총 크기
j = 0
answer = [0 for _ in range(n)]
for i in range(n):
    while arr[j][0] < arr[i][0]:
        prefix[arr[j][1]] += arr[j][0]
        total += arr[j][0]
        j += 1
    answer[arr[i][2]] = total - prefix[arr[i][1]] # 총합 - 현재 색깔 공 누적합(같은 색깔은 못잡으므로)
for i in range(n):
    print(answer[i])