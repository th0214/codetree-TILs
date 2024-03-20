from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dice = [1,2,3,4,5,6]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = 0
x,y = 0, 0
result = 0

def score(nx, ny, graph):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((nx,ny))
    visited[nx][ny] = 1
    standard = graph[nx][ny]
    cnt = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]

            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0:
                if graph[xx][yy] == standard:
                    visited[xx][yy] = 1
                    q.append((xx,yy))
                    cnt += 1
    return cnt * standard

def move(x,y,d):
    global dice

    # 동쪽
    if dir == 0:
        dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    # 남쪽
    elif dir == 1:
        dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    # 서쪽
    elif dir == 2:
        dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    # 북쪽
    else:
        dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]

    if graph[nx][ny] > dice[5]:
            d = (d-1) % 4

    elif graph[nx][ny] < dice[5]:
            d = (d+1) % 4

    return d

for _ in range(m):

    nx = x + dx[d]
    ny = y + dy[d]
    
    if not (0 <= nx < n and 0 <= ny < n):
        nx = x + dx[d] * (-1)
        ny = y + dy[d] * (-1)
        d = (d+2) % 4

    d = move(nx,ny,d)
    x,y = nx, ny
    result += score(nx,ny,graph)

print(result)