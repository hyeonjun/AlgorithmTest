"""
ex1) min=5, max=10
2의 제곱수인 4
5 // 4 = 1 로 배수를 1로 잡게 되면
4부터 시작하게 되면서 인덱스 범위에 맞춰지지 않음
5 % 4 = 1로 min 값이 제곱수에 나누어 떨어지지 않으므로
배수 값을 5 // 4 + 1로 해야함
=> 4 * (5 // 4 + 1) = 4 * 2 = 8이 되어 범위 안에 맞춰짐

ex2) min=11, max=20
11 // 4 = 2
4 * 2 = 8 -> 범위에 맞지 않음
11 % 4 = 3 -> 나누어 떨어지지 않으므로
배수를 +1 해주면 12부터 시작하게 되어 범위 안에 맞춰짐
"""

x, y = map(int, input().split())
check = [1 for _ in range(y-x+1)]
n = 2
while n * n <= y:
    squared_num = n * n
    mul = x // squared_num if not x % squared_num else x // squared_num + 1 # 배수
    while squared_num * mul <= y:
        if check[squared_num * mul - x]:
            check[squared_num * mul - x] = 0
        mul += 1
    n += 1
print(sum(check))