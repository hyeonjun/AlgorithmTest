# 마방진의 합 = n * (n^2 + 1) / 2
def odd(n): # 홀수
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, n // 2 # 시작 지점 -> 첫행 중간에 1을 둔다
    for i in range(1, n*n+1):
        arr[x][y] = i
        if i % n == 0: # 테이블에 들어간 수가 n의 배수이면 행만 증가
            x += 1
        else:
            # 오른쪽 아래쪽
            x -= 1 # 행 감소
            y += 1 # 열 증가
            if x < 0: # 행이 첫 행보다 작아지는 경우, 마지막 행으로 이동
                x = n-1
            if y > n-1: # 열이 끝 열을 넘어가는 경우, 첫 열로 이동
                y = 0
    return arr

def even(n): # 4의 배수가 아닌 짝수, 이해안된다.
    arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n//2):
        for j in range(n//2):
            if j < (n//4):
                arr[i][j] = 3
    arr[n//4][0] = 0
    arr[n//4][n//4] = 3

    for i in range(n//2, n):
        for j in range(n//2):
            if arr[i-n//2][j] == 0:
                arr[i][j] = 3

    for i in range(n//2):
        for j in range(n//2, n):
            arr[i][j] = 1 if n - (n//4 - 1) - 1 < j else 2

    for i in range(n//2, n):
        for j in range(n//2, n):
            arr[i][j] = 2 if arr[i-n//2][j] == 1 else 1

    for i in range(n):
        for j in range(n):
            arr[i][j] *= (n * n // 4)

    x, y, = 0, 0
    odd_r = odd(n // 2)

    for i in range(n):
        for j in range(n):
            arr[i][j] += odd_r[x][y]
            y += 1
            if y >= n//2:
                y = 0
        x += 1
        if x >= n//2:
            x = 0
    return arr

def fourmul(n): # 4의 배수
    num = 1
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = num
            num += 1
    # 4의 배수 마방진은 k:2k:k 비율로 나누어야 한다.
    # 4 -> 1, 2, 1 | 8 -> 2, 4, 2 | 12 - > 3, 6, 3 ..
    # 결국 비율은 25%, 50%, 25% 이므로
    # tmp1 / n * 100 = 25% => tmp1 = 25 * n / 100
    # tmp2 / n * 100 = 50% => tmp2 = 50 * n / 100
    tmp1, tmp2 = 25 * n // 100, 50 * n // 100

    def swap(t1, t2, n):
        # 스왑
        # (0,1),(3,2)  (0,2),(3,1) => 행 고정 -> 열 변경
        # (1,0),(2,3)  (2,0),(1,3) => 열 고정 -> 행 변경
        arr[t1][t2], arr[n-1-t1][n-1-t2] = arr[n-1-t1][n-1-t2], arr[t1][t2]
        arr[t2][t1], arr[n-1-t2][n-1-t1] = arr[n-1-t2][n-1-t1], arr[t2][t1]

    # 나눈 후 스왑.
    # 0    1 2     3 -> range(tmp1(1) ~ tmp1(1)+tmp2(2))
    # 0 1    2 3 4 5    6 7 -> range(tmp1(2) ~ tmp1(2)+tmp2(4)) 범위
    for i in range(tmp1):
        for j in range(tmp1, tmp1+tmp2):
            swap(i, j, n)
    return arr

n = int(input())
result = odd(n) if n % 2 == 1 else fourmul(n) if n % 4 == 0 else even(n)
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()