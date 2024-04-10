from collections import deque

n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dice = [1,6,4,3,2,5] # 상하좌우대1대2
direction = 0
now = [0,0]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = 0

def move():
    global direction, now, dice

    nx, ny = now[0]+dx[direction], now[1]+dy[direction]

    if 0 <= nx < n and 0 <= ny < n:

        if direction == 0:
            dice = [dice[2],dice[3],dice[1],dice[0],dice[4],dice[5]]
        elif direction == 1:
            dice = [dice[5],dice[4],dice[2],dice[3],dice[0],dice[1]]
        elif direction == 2:
            dice = [dice[3],dice[2],dice[0],dice[1],dice[4],dice[5]]
        elif direction == 3:
            dice = [dice[4],dice[5],dice[2],dice[3],dice[1],dice[0]]
        
        c_point(nx,ny)
        now = [nx, ny]
        if dice[1] > graph[nx][ny]:
            direction = (direction+1) % 4
        elif dice[1] < graph[nx][ny]:
            direction = (direction-1) % 4

    else:
        direction = (direction+2) % 4

        nx, ny = now[0] + dx[direction], now[1] + dy[direction]

        if direction == 0:
            dice = [dice[2],dice[3],dice[1],dice[0],dice[4],dice[5]]
        elif direction == 1:
            dice = [dice[5],dice[4],dice[2],dice[3],dice[0],dice[1]]
        elif direction == 2:
            dice = [dice[3],dice[2],dice[0],dice[1],dice[4],dice[5]]
        elif direction == 3:
            dice = [dice[4],dice[5],dice[2],dice[3],dice[1],dice[0]]
        
        c_point(nx,ny)
        now = [nx, ny]
        if dice[1] > graph[nx][ny]:
            direction = (direction+1) % 4
        elif dice[1] < graph[nx][ny]:
            direction = (direction-1) % 4

def c_point(x,y):
    global result

    q = deque()
    visited = [[0] * n for _ in range(n)]
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    number = graph[x][y]

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == number:
                visited[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1

    result += (number*cnt)



for _ in range(m):
    move()

print(result)