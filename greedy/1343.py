#폴리오미노
#그리디 형식으로 푼건 아님 이건
board = input()

board = board.replace('XXXX','AAAA')
board = board.replace('XX','BB')

if 'X' in board:
    print(-1)
else:
    print(board)
