# 브루트포스
def FourSquares(n):
    min_ = 4
    for i in range(int(n ** 0.5), int((n // 2) ** 0.5) - 1, -1):
        x = n - i * i
        if x == 0:
            return 1

        for j in range(int(x ** 0.5), int((x // 2) ** 0.5) - 1, -1):
            y = x - j * j
            if y == 0:
                min_ = min(min_, 2)
                break

            for k in range(int(y ** 0.5), int((y // 2) ** 0.5) - 1, -1):
                z = y - k * k
                if z == 0:
                    min_ = min(min_, 3)
                    break
    return min_
print(FourSquares(int(input())))

# DP
n = int(input())
dp = [0, 1]
for i in range(2, n+1):
    min_ = float('inf')
    j = 1

    while (j ** 2) <= i:
        min_ = min(min_, dp[i - (j**2)])
        j += 1

    dp.append(min_ + 1)
print(dp[n])