N, M, K = map(int, input().split())

gunBoard = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 0:
            continue
        gunBoard[i][j].append(row[j])

# x, y, dir, str, gun
playersList = list()
playersBoard = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(M):
    x, y, d, s = map(int, input().split())
    playersList.append([x - 1, y - 1, d, s, 0])
    playersBoard[x - 1][y - 1] = i

scores = [0 for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def rotateDirection(d):
    if d + 1 < 4:
        return d + 1
    return 0

def flipDirection(d):
    if d == 0:
        return 2
    if d == 1:
        return 3
    if d == 2:
        return 0
    if d == 3:
        return 1
    return d

def isVaild(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def getMoveCoordinate(i):
    x, y = playersList[i][0], playersList[i][1]
    nx, ny = x + dx[playersList[i][2]], y + dy[playersList[i][2]]
    if not isVaild(nx, ny):
        playersList[i][2] = flipDirection(playersList[i][2])
        nx, ny = x + dx[playersList[i][2]], y + dy[playersList[i][2]]
    return nx, ny

def move(playerIndex, nx, ny):
    x, y = playersList[playerIndex][0], playersList[playerIndex][1]
    playersBoard[x][y] = -1
    
    playersBoard[nx][ny] = playerIndex
    playersList[playerIndex][0], playersList[playerIndex][1] = nx, ny
    return

def getGun(playerIndex, nx, ny):
    if playersList[playerIndex][4] == 0:
        playersList[playerIndex][4] = max(gunBoard[nx][ny])
        gunBoard[nx][ny].pop(gunBoard[nx][ny].index(max(gunBoard[nx][ny])))
    else:
        maxGun = max(gunBoard[nx][ny])
        playerGun = playersList[playerIndex][4]
        if playerGun >= maxGun:
            return
        playersList[playerIndex][4] = max(gunBoard[nx][ny])
        gunBoard[nx][ny][gunBoard[nx][ny].index(max(gunBoard[nx][ny]))] = playerGun
    return


def fight(player1Index, player2Index):
    if playersList[player1Index][3] + playersList[player1Index][4] > playersList[player2Index][3] + playersList[player2Index][4]:
        return player1Index, player2Index, abs(playersList[player1Index][3] + playersList[player1Index][4] - playersList[player2Index][3] - playersList[player2Index][4])
    elif playersList[player1Index][3] + playersList[player1Index][4] < playersList[player2Index][3] + playersList[player2Index][4]:
        return player2Index, player1Index, abs(playersList[player1Index][3] + playersList[player1Index][4] - playersList[player2Index][3] - playersList[player2Index][4])
    else:
        if playersList[player1Index][3] > playersList[player2Index][3]:
            return player1Index, player2Index, abs(playersList[player1Index][3] + playersList[player1Index][4] - playersList[player2Index][3] - playersList[player2Index][4])
        else:
            return player2Index, player1Index, abs(playersList[player1Index][3] + playersList[player1Index][4] - playersList[player2Index][3] - playersList[player2Index][4])

def dropAllGuns(playerIndex, nx, ny):
    gunBoard[nx][ny].append(playersList[playerIndex][4])
    playersList[playerIndex][4] = 0

def getLoserMovement(i):
    x, y = playersList[i][0], playersList[i][1]
    nx, ny = x + dx[playersList[i][2]], y + dy[playersList[i][2]]
    while not (isVaild(nx, ny) and playersBoard[nx][ny] == -1) :
        playersList[i][2] = rotateDirection(playersList[i][2])
        nx, ny = x + dx[playersList[i][2]], y + dy[playersList[i][2]]
    return nx, ny

def play():
    for i in range(M):
        nx, ny = getMoveCoordinate(i)
            
        if playersBoard[nx][ny] == -1:
            if len(gunBoard[nx][ny]) == 0:
                move(i, nx, ny)
                continue
            getGun(i, nx, ny)
            move(i, nx, ny)
        else:

            winnerIndex, loserIndex, scoreDiff = fight(i, playersBoard[nx][ny])
            scores[winnerIndex] += scoreDiff
            move(i, nx, ny)
            # 진 플레이어
            dropAllGuns(loserIndex, nx, ny)
            lx, ly = getLoserMovement(loserIndex)
            move(loserIndex, lx, ly)
            if len(gunBoard[lx][ly]) != 0:
                getGun(loserIndex, lx, ly)
            
            # 이긴 플레이어
            getGun(winnerIndex, nx, ny)
            playersBoard[nx][ny] = winnerIndex
    return


for _ in range(K):
    play()

for i in scores:
    print(i, end=" ")