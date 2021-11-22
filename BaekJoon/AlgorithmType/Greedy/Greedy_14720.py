# 딸기 -> 초코 -> 바나나 -> 딸기
n = int(input())
arr = list(map(int, input().split()))
answer = 0
milk = [0, 1, 2]
idx = 0
for i in arr:
    if i == milk[idx]:
        answer+=1
        idx = (idx+1)%3
print(answer)