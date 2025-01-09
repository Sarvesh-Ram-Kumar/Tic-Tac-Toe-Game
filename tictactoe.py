def position():
    while True:
        position=int(input("pick a position:"))
        if position not in range(1,10):
            print("invalid input")
        else:
            return position
            break
def display_board(b):
    print(b[1]+'      |'+b[2]+'      |'+b[3])
    print("______  ______  _______")
    print(b[4]+'      |'+b[5]+'      |'+b[6])
    print("______  ______  _______")
    print(b[7]+'      |'+b[8]+'      |'+b[9])
def check():
    if board[1]==board[2]==board[3] or board[4]==board[5]==board[6] or board[7]==board[8]==board[9] or board[1]==board[4]==board[7] or board[2]==board[5]==board[8] or board[3]==board[6]==board[9] or board[1]==board[5]==board[9] or board[7]==board[5]==board[3]:
        return True
    elif board[1]!='1'and board[2]!='2'and board[3]!='3'and board[4]!='4'and board[5]!='5'and board[6]!='6'and board[7]!='7'and board[8]!='8'and board[9]!='9':
        return 'Draw'
    else:
        return False
def Game(b,p):
    num=0
    if player1=='X':
        while True:
            if num%2==0:
                b[p]='X'
                display_board(b)
                num+=1
                c=check()
                if c==True:
                    print("Player1 won")
                    break
                elif c=='Draw':
                    print("Draw")
                    break
                p=position()
            else:
                b[p]='O'
                display_board(b)
                num+=1
                c=check()
                if c==True:
                    print("Player2 won")
                    break
                elif c=='Draw':
                    print("Draw")
                    break
                p=position()
    else:
        while True:
            if num%2==0:
                b[p]='O'
                display_board(b)
                num+=1
                c=check()
                if c==True:
                    print("Player1 won")
                    break
                elif c=='Draw':
                    print("Draw")
                    break
                p=position()
            else:
                b[p]='X'
                display_board(b)
                num+=1
                c=check()
                if c==True:
                    print("Player2 won")
                    break
                elif c=='Draw':
                    print("Draw")
                    break
                p=position()
while True:
    while True:
        player1=input("pick marker (X or O):")
        if player1 not in['X','O']:
            print("invalid input")
        else:
            break
    board=['','1','2','3','4','5','6','7','8','9']
    l=position()
    Game(board,l)
    choice=input("Do you want another game(y/n):")
    if choice=="n":
        break
