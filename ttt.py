import sympy as sp

x1 = 1
x2 = 2
x3 = 3
x4 = 4
x5 = 5
x6 = 6
x7 = 7 
x8 = 9
x9 = 9 

ttt = [0,1,2,3,4,5,6,7,8,9]

def field(ttt):
    print(f'-----\n{ttt[1]}|{ttt[2]}|{ttt[3]}\n-|-|-\n{ttt[4]}|{ttt[5]}|{ttt[6]}\n-|-|-\n{ttt[7]}|{ttt[8]}|{ttt[9]}\n-----\n')
    
def win_player(player,ttt):
    if (player == ttt[1] and player == ttt[2] and player == ttt[3]) \
        or (player == ttt[4] and player == ttt[5] and player == ttt[6]) \
        or (player == ttt[7] and player == ttt[8] and player == ttt[9]) \
        or (player == ttt[1] and player == ttt[5] and player == ttt[9]) \
        or (player == ttt[3] and player == ttt[5] and player == ttt[7]) \
        or (player == ttt[1] and player == ttt[4] and player == ttt[7]) \
        or (player == ttt[2] and player == ttt[5] and player == ttt[8]) \
        or (player == ttt[3] and player == ttt[6] and player == ttt[9]):
        return True
    else:
        return False
    


side = str()
me = str()
enemy = str()
player1 = 'X'
player2 = 'O'



move = 0
player = player1
while move < 9:
    move += 1
    if win_player(player,ttt) == True:
        print(f'\n\n\n\n{player}{player}{player}{player}{player}{player}{player}{player}{player}{player}\n!!! WIN !!!\n\n')
        move == 9
        break
    if move % 2 == 0:
        player = player2
    else:
        player = player1

    while True:
        field(ttt)
        number = input(f'\n\n\nWrite your number -- {player} -- :\nNUMBER: ')
        try:
            if int(number) in ttt:
                ttt[int(number)] = player
                break
        except:
            1
if win_player(player,ttt) == True:
    print(f'\n\n\n\n{player}{player}{player}{player}{player}{player}{player}{player}{player}{player}\n!!! WIN !!!')
    move == 9
    
else:
    if move >= 9:
        print("\n\n\n\n!!! DRAW !!!\n\n")
    
field(ttt)