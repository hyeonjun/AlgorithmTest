"""
비트마스크
ex), {1, 3, 4, 5, 9}를 사용한다할 때, 01000111010 정수로 표현할 수 있다.
 => binary digit이 0부터 시작한다고 할 때, 1, 3, 4, 5, 9번째 자리를 1로 표시한 것

board에 숫자가 총 n * m개있으므로 각각을 자릿수로하는 n*m-1 자리 정수를 만든다.
그래서 각 자리에 0, 1로 표시하여 세로는 0, 가로는 1로 자른다고 가정.
"""
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
answer = 0

for i in range(1 << n*m):
    result = 0
    # 가로 합 계산
    for row in range(n):
        row_sum = 0
        for col in range(m):
            idx = row * m + col
            if i & (1 << idx) != 0: # 1은 가로
                row_sum = row_sum * 10 + board[row][col]
            else:
                result += row_sum
                row_sum = 0
        result += row_sum

    # 세로 합 계산
    for col in range(m):
        col_sum = 0
        for row in range(n):
            idx = row * m + col
            if i & (1 << idx) == 0: # 0은 세로
                col_sum = col_sum * 10 + board[row][col]
            else:
                result += col_sum
                col_sum = 0
        result += col_sum
    answer = max(answer, result)

print(answer)