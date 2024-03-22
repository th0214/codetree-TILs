from collections import deque

n, m, k, c = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
sp = [[0] * n for _ in range(n)]
result = 0

def grow(x,y):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    q = deque()
    q.append((x,y))
    cnt = 0
    while q:
        i,j = q.popleft()

        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]

            if 0 <= ni < n and 0 <= nj < n:
                if graph[ni][nj] > 0:
                    cnt += 1

    graph[i][j] += cnt 

def bunsik(i,j,tmp):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    location = []
    q = deque()
    q.append((i,j))
    cnt = 0
    while q:
        i,j = q.popleft()

        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]

            if 0 <= ni < n and 0 <= nj < n:
                if graph[ni][nj] == 0 and sp[ni][nj] == 0:
                    cnt += 1
                    location.append([ni,nj])
    for x,y in location:
        tmp[x][y] += (graph[i][j] // cnt)

def check_kill(i,j,killer):
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]

    q = deque()
    q.append((i,j))
    cnt = graph[i][j]

    while q:
        x,y = q.popleft()

        for j in range(4):
            for i in range(1,k+1):
                nx = x + dx[j] * i
                ny = y + dy[j] * i

                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > 0:
                        cnt += graph[nx][ny]
                    if graph[nx][ny] == -1 or graph[nx][ny] == 0:
                        break
    
    if killer[0][2] < cnt:
        killer.pop()
        killer.append([x,y,cnt])

def kill(killer):
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]
    i,j = killer[0][0], killer[0][1]

    q = deque()
    q.append((i,j))
    sp[i][j] = c+1

    while q:
        x,y = q.popleft()

        for i in range(4):
            for j in range(1,k+1):
                nx = x + (dx[i] * j)
                ny = y + (dy[i] * j)

                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > 0:
                        sp[nx][ny] = c+1
                    if graph[nx][ny] == -1:
                        break
                    if graph[nx][ny] == 0:
                        sp[nx][ny] = c+1
                        break
    for i in range(n):
        for j in range(n):
            if sp[i][j] > 0:
                graph[i][j] = 0

def minus():
    for i in range(n):
        for j in range(n):
            if sp[i][j] > 0:
                sp[i][j] -= 0

for _ in range(m):
    tmp = [[0] * n for _ in range(n)]
    killer = [[0,0,0]]
    sp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                grow(i,j)
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                bunsik(i,j,tmp)
    
    for i in range(n):
        for j in range(n):
            graph[i][j] += tmp[i][j]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                check_kill(i,j,killer)

    kill(killer)
    minus()
    result += killer[0][2]

print(result)