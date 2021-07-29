# 꽃길
def solution(n, price):
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    flower_bed = [[0 for _ in range(n)] for _ in range(n)]
    sum_price = []
    answer = 0
    cnt = 0
    for r in range(1, n-1):
        for c in range(1, n-1):
            tmp = 0
            for dx, dy in move:
                nx, ny = dx+r, dy+c
                tmp += price[nx][ny]
            sum_price.append([(r,c), tmp+price[r][c]])
    sum_price.sort(key=lambda x : x[1])

    def check(x, y):
        for dx, dy in move:
            nx, ny = dx + x, dy + y
            if flower_bed[nx][ny] == 1:
                return False
        return True

    for idx, v in sum_price:
        x, y = idx[0], idx[1]
        if flower_bed[x][y] == 0 and check(x, y):
            flower_bed[x][y] = 1
            for dx, dy in move:
                nx, ny = dx + x, dy + y
                flower_bed[nx][ny] = 1
            answer += v
            cnt += 1
            if cnt == 3:
                return answer

    return answer

price = [
    [1, 0, 2, 3, 3, 4],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1],
    [3, 9, 9, 0, 1, 99],
    [9, 11, 3, 1, 0, 3],
    [12, 3, 0, 0, 0, 1],
]
print(solution(6, price)) # 12

def solution(n, price):
    ans = 10000

    def ck(lst):
        move = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []
        cnt = 0
        for flower in lst:
            x = flower // n
            y = flower % n
            if x == 0 or x == n-1 or y == 0 or y == n-1:
                return 10000
            for dx, dy in move:
                result.append((x+dx, y+dy))
                cnt += price[x+dx][y+dy]
        if len(set(result)) != 15:
            return 10000
        return cnt


    for i in range(n*n):
        for j in range(i+1, n*n):
            for k in range(j+1, n*n):
                ans = min(ans, ck([i, j, k]))
    return ans

price = [
    [1, 0, 2, 3, 3, 4],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1],
    [3, 9, 9, 0, 1, 99],
    [9, 11, 3, 1, 0, 3],
    [12, 3, 0, 0, 0, 1],
]
print(solution(6, price))
