a = int(input()) # 현재 고기 온도
b = int(input()) # 목표 온도
c = int(input()) # 얼어있는 고기를 1도 데우는데 걸리는 시간
d = int(input()) # 얼어있는 고기를 해동하는데 걸리는 시간
e = int(input()) # 얼어 있지 않은 고기를 1도 데우는데 걸리는 시간
answer = 0
if a < 0:
    answer += (0-a) * c
    a = 0
if a == 0:
    answer += d
if 0 <= a < b:
    answer += (b-a) * e
print(answer)