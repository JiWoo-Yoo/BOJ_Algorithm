answer = '-1'
board = input()
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')
if 'X' not in board:
    answer = board
    
print(answer)