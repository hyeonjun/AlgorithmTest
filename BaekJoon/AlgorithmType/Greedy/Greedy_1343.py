board = input()
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')
if board.count('X') > 0:
    print(-1)
else:
    print(board)

