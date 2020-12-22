player1 = []
player2 = []
ll = [x for x in open('input22.txt').read().strip().split('\n\n')]
for i in ll:
    i = i.split("\n")
    if '' in i:
        i.remove('')
    if "Player 1:" in i:
        player1 = i[1:]
    else:
        player2 = i[1:]

def playerWins(player):
    mul = 0
    for i in range(1, len(player) + 1):
        mul += (int(player[i - 1]) * ((len(player) + 1) - i))
    print(mul)

def playerRoundwin(player_, player__):
    player_.append(player_[0])
    player_.append(player__[0])
    del player_[0]
    del player__[0]
    return player_, player__

while True:
    if not player1:
        playerWins(player2)
        break
    if not player2:
        playerWins(player1)
        break

    elif int(player1[0]) > int(player2[0]):
        player1, player2 = playerRoundwin(player1, player2)

    elif int(player2[0]) > int(player1[0]):
        player2, player1 = playerRoundwin(player2, player1)


