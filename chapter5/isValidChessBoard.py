def isValidChessBoard(chessBoard):
    board=[]
    for i in range(1,9):
        for j in range(97,106):
            k = chr(j)
            boardItem=str(i)+str(k)
            board.append(boardItem)

    chess=[]
    for i in 'w', 'b':
        for j in ['pwan', 'knight', 'bishop', 'rook', 'queen', 'king']:
            chessItem=i+j
            chess.append(chessItem)


    for k, v in chessBoard.items():
        if k in board:
            if v in chess:
                continue
            else:
                print("These is a wrong chessValue at leat")
                break
        else:
            print("These is a wrong chessBoardValue at least")
            break

    wnum = 0
    bnum = 0
    wpawn_num = 0
    bpawn_num = 0
    for k, v in chessBoard.items():
        if v[0]=='w':
            wnum=wnum+1
        elif v[0]=='b':
            bnum=bnum+1


        if v == 'wpawn':
            wpawn_num = wpawn_num + 1
        elif v == 'bpawn':
            bpawn_num = bpawn_num + 1

    if wpawn_num > 8 or bpawn_num > 8 or wnum>16 or bnum>16:
        print('Each player can only have at most 16 pieces, at most 8 pawns.')
    print("check over")
mychess={'1h': 'bking', '8c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
isValidChessBoard(mychess)
seventeenBPieces = {'1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bbishop', '1f': 'bbishop', '1g': 'bbishop', '1h': 'bbishop', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '3a': 'bpawn', '8a': 'wking', '8b': 'wqueen', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wbishop', '8f': 'wbishop', '8g': 'wbishop', '8h': 'wbishop', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn'}
isValidChessBoard(seventeenBPieces)
