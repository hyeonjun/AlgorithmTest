n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

answer = -1
for i in range(n-2): # 세 변 중 가장 긴 변의 길이가 나머지 두 변의 길이보다 커야함
    if arr[i] < arr[i+1] + arr[i+2]: # 삼각형 각 변의 길이를 a, b, c이고 가장 긴 변이 a일때 a < b+c를 만족해야 함
        answer = arr[i] + arr[i+1] + arr[i+2]
        break
print(answer)