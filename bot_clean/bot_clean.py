#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    dBairlaluud = bairlaluudAvya(board)
    mur = dBairlaluud[0]
    bagana = dBairlaluud[1]
    if posr < mur:
        posr += 1
        print('DOWN')
    elif posr > mur:
        posr -= 1
        print('UP')
    elif posc < bagana:
        posc += 1
        print('RIGHT')
    elif posc > bagana:
        posc -= 1
        print('LEFT')
    else:
        print('CLEAN')
    

def bairlaluudAvya(board):
    khemjee = len(board)
    butsaakhJagsaalt = []
    for mur in range(khemjee):
        for bagana in range(khemjee):
            if board[mur][bagana] == 'd':
                return (mur,bagana)
                break
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)