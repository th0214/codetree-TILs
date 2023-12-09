from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    
finishedCnt = 0
people = []
for _ in range(M):
    a, b = map(int, input().split())
    people.append([-1, -1, a - 1, b - 1])
    
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def isValid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def findMovements(sx, sy, ex, ey):
    visited = [[False for _ in range(N)] for _ in range(N)]
    back_x = [[-1 for _ in range(N)] for _ in range(N)]
    back_y = [[-1 for _ in range(N)] for _ in range(N)]
    visited[sx][sy] = True
    q = deque()
    q.append([sx, sy])
    while q:
        x, y = q.popleft()
        
        if x == ex and y == ey:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx, ny) and not visited[nx][ny] and board[nx][ny] != -1:
                back_x[nx][ny] = x
                back_y[nx][ny] = y
                visited[nx][ny] = True
                q.append([nx, ny])

    cx, cy = ex, ey
    while True:
        if back_x[cx][cy] == sx and back_y[cx][cy] == sy:
            break
        tempX, tempY = cx, cy
        cx = back_x[tempX][tempY]
        cy = back_y[tempX][tempY]
    
    return [cx, cy]
        
def isSameCoordinates(a: list):
    return a[0] == a[2] and a[1] == a[3]

def moveToStore():
    global finishedCnt
    for i in range(len(people)):
        if people[i][0] != -1 and not isSameCoordinates(people[i]):
            people[i][0] , people[i][1]  = findMovements(people[i][0], people[i][1], people[i][2], people[i][3])
    
            if isSameCoordinates(people[i]):
                board[people[i][0]][people[i][1]] = -1
                finishedCnt += 1
    return

def findBaseCampCoordinates(cx, cy):
    coordinates = []
    q = deque()
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    dist[cx][cy] = 0
    q.append([cx, cy])
    
    d = 1
    found = False
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if isValid(nx, ny) and board[nx][ny] != -1 and dist[nx][ny] == -1:
                    if board[nx][ny] == 1:
                        coordinates.append([nx, ny])
                        found = True
                    dist[nx][ny] = d
                    q.append([nx, ny])
        d += 1            
        if found:
            break
    coordinates.sort()
    return coordinates[0]

def moveToBaseCamp(t):
    bx, by = findBaseCampCoordinates(people[t - 1][2], people[t - 1][3])
    board[bx][by] = -1
    people[t - 1][0], people[t - 1][1] = bx, by
    return

t = 0
while finishedCnt != M:
    t += 1
    moveToStore()
    
    if t <= M:
        moveToBaseCamp(t)
    
print(t)