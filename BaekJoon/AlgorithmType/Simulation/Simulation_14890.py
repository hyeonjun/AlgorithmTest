n, l = map(int, input().split())
board= [list(map(int, input().split())) for _ in range(n)]
answer = 0

def check(arr):
    flag = [False for _ in range(n)]
    for i in range(n-1):
        if arr[i] == arr[i+1]: # 같은 높이
            continue
        if abs(arr[i] - arr[i+1]) > 1: # 높이가 2이상 차이 나면 안됨
            return False
        if arr[i] > arr[i+1]: # ex) 2 1 1
            height = arr[i+1]
            for j in range(i+1, i+1+l):
                if j < n:
                    if arr[j] != height: # 다리 설치 중에 높이가 다르면
                        return False
                    if flag[j]: # 이미 설치했으면
                        return False
                    flag[j] = True
                else:
                    return False
        else: # ex) 1 1 2
            height = arr[i]
            for j in range(i, i-l, -1):
                if 0 <= j:
                    if arr[j] != height:
                        return False
                    if flag[j]:
                        return False
                    flag[j] = True
                else:
                    return False
    return True

for b in board: # 가로
    if check(b):
        answer += 1

for b in zip(*board): # 세로
    if check(b):
        answer += 1
print(answer)