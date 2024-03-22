from collections import deque
from copy import deepcopy
n, m, k, c = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
sp = [[0] * n for _ in range(n)]
result = 0

def grow(x,y):
    tmp = [[0] * n for _ in range(n)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    cnt = 0
    
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > 0:
                tmp[x][y] += 1

    for i in range(n):
        for j in range(n):
            graph[i][j] += tmp[i][j]

def bunsik():
    tmp = deepcopy(graph)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                cnt = 0

                for a in range(4):
                    nx, ny = i + dx[a], j + dy[a]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and sp[nx][ny] == 0:
                        cnt += 1
                        
                if cnt != 0:
                    tmp_cnt = graph[i][j] // cnt
                    
                    for a in range(4):
                        nx, ny = i + dx[a], j + dy[a]
                        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and sp[nx][ny] == 0:
                            tmp[nx][ny] += tmp_cnt
    
    return tmp

def check_kill(i,j,killer):
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]

    cnt = graph[i][j]
    x,y = i,j
    for i in range(4):
        for j in range(1,5):
            nx = x + dx[i] * j
            ny = y + dy[i] * j

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0:
                    cnt += graph[nx][ny]
                if graph[nx][ny] == -1 or graph[nx][ny] == 0:
                    break
            else:
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


    x,y = q.popleft()

    for i in range(4):
        cur_x, cur_y = x,y
        for j in range(k):
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
                sp[i][j] -= 1

for _ in range(m):
    killer = [[0,0,0]]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                grow(i,j)
    
    graph = bunsik()

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                check_kill(i,j,killer)

    kill(killer)
    minus()
    result += killer[0][2]

print(result)