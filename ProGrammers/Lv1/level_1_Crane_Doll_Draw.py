def solution(board, moves):
    answer = 0
    basket = []
    N = len(board)
    for i in moves:
        for j in range(N):
            if board[j][i-1] != 0:
                if len(basket) > 0 and basket[-1] == board[j][i-1]:
                    basket.pop() # pop()는 가장 나중에 들어온 값부터 처리.
                    answer += 2
                else:
                    basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
            if j == N - 1 and board[j][i-1] == 0:
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
"""
 0 4 2 4 0 1 0 3
[[0,0,0,0,0],
 [0,0,1,0,3],
 [0,2,5,0,1],
 [4,2,4,4,2],
 [3,5,1,3,1]] 4 
"""

def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y>0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m-1].pop(0)) == (l:= s.pop()):
                a+=2
            else:
                s.extend([l, d])
    return a

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                   [1, 5, 3, 5, 1, 2, 1, 4]))