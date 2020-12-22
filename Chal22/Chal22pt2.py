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

def playerwins(player):
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

def recurse(player1, player2, prevRoundsMemory):
    while True:
        if not player1:
            return 2
        if not player2:
            return 1

        if player1 in prevRoundsMemory and player2 in prevRoundsMemory:
            return 1
        else:
            prevRoundsMemory.append(player1.copy())
            prevRoundsMemory.append(player2.copy())

        if int(player1[0]) <= len(player1[1:]) and int(player2[0]) <= len(player2[1:]):
            newPlayer1 = player1[1:int(player1[0])+1]
            newPlayer2 = player2[1:int(player2[0])+1]
            won = recurse(newPlayer1, newPlayer2, [])
            if won == 1:
                player1, player2 = playerRoundwin(player1, player2)
            else:
                player2, player1 = playerRoundwin(player2, player1)

        elif int(player1[0]) > int(player2[0]):
            player1, player2 = playerRoundwin(player1, player2)

        elif int(player2[0]) > int(player1[0]):
            player2, player1 = playerRoundwin(player2, player1)

player = recurse(player1, player2, [])
if player == 1:
    playerwins(player1)
else:
    playerwins(player2)