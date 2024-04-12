N,M,k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

directions = list(map(int, input().split()))

prior = []
for i in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    prior.append(temp)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

smell = [[[0,0] for _ in range(N)] for _ in range(N)]

def update_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

            if board[i][j] != 0:
                smell[i][j] = [board[i][j], k]

def move():
    tmp_board = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if board[x][y] != 0:
                direction = directions[board[x][y]-1]
                found = False
                for idx in prior[board[x][y]-1][direction-1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][1] == 0:
                            directions[board[x][y] - 1] = idx
                            if tmp_board[nx][ny] == 0:
                                tmp_board[nx][ny] = board[x][y]
                            else:
                                tmp_board[nx][ny] = min(tmp_board[nx][ny], board[x][y])
                            found =True
                            break
                if found:
                    continue

                for idx in prior[board[x][y]-1][direction-1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][0] == board[x][y]:
                            directions[board[x][y]-1] = idx
                            tmp_board[nx][ny] = board[x][y]
                            break
    return tmp_board

answer = 0

while True:
    update_smell()
    board = move()
    answer += 1
    check =True
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1:
                check =False

    if check:
        print(answer)
        break

    if answer >= 1000:
        print(-1)
        break