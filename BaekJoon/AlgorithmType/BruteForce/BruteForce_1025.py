n, m = map(int, input().split())
nums = [list(map(int, list(input()))) for _ in range(n)]
answer = -1

for i in range(n): # 행
    for j in range(m): # 열
        for wx in range(-n, n): # 행의 공차, 음수도 가능하므로 -n부터
            for wy in range(-m, m): # 열 공차
                if wx == wy == 0: continue # 두 공차가 모두 0이면 계속 같은 위치만 나오기 때문에 넘어가야한다.
                x, y = i, j
                step = 0
                num = ''
                while 0 <= x < n and 0 <= y < m:
                    num += str(nums[x][y])
                    step += 1

                    # 제곱수 확인
                    sqrt = int(num) ** 0.5
                    if sqrt == int(sqrt):
                        answer = max(answer, int(num))

                    # 등차수열 an = ax + (n-1) * d
                    x = i + step * wx
                    y = j + step * wy
print(answer)
