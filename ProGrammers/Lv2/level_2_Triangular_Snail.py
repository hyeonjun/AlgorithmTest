def solution(n):
    answer = [[0] * i for i in range(1, n+1)]
    x, y = -1, 0
    count = 1
    for i in range(n): # 움직이는 방향은 하, 우, 상 세가지 임
        for j in range(i, n): # 한 방향으로 끝까지 갈때마다의 해당 갯수는 n에 1씩 감소한것과 같다.
            if i % 3 == 0:  # n이 4일때,  4 -> 하(i=0, j=0~3), 3 -> 우(i=1, j=1~3), 2 -> 상(i=2, j=2~3), 1 -> 하(i=3, j=3)
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = count
            count += 1
    return sum(answer, [])

print(solution(4)) # [1,2,9,3,10,8,4,5,6,7]
print(solution(5)) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6)) # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]