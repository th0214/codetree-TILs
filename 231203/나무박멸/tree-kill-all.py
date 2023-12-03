from copy import deepcopy
n, m, k, c = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
answer = 0
visited = [[0] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ddx = [-1, -1, 1, 1]
ddy = [-1, 1, -1, 1]


def grow():
    tmp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:

                for a in range(4):
                    nx, ny = i + dx[a], j + dy[a]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                        tmp[i][j] += 1
    
    for i in range(n):
        for j in range(n):
            graph[i][j] += tmp[i][j]
                

def seed():
    tmp = deepcopy(graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                cnt = 0

                for a in range(4):
                    nx, ny = i + dx[a], j + dy[a]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                        cnt += 1
                        
                if cnt != 0:
                    tmp_cnt = graph[i][j] // cnt
                    
                    for a in range(4):
                        nx, ny = i + dx[a], j + dy[a]
                        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                            tmp[nx][ny] += tmp_cnt
    
    return tmp


def killer(x,y):
    global score, max_x, max_y

    value = graph[x][y] # 제초제로 죽일 수 있는 나무의 양

    for p in range(4):
        cur_x, cur_y = x, y
        for _ in range(k):

            mx = cur_x + ddx[p]
            my = cur_y + ddy[p]

            if not (0 <= mx < n and 0 <= my < n):
                break

            if graph[mx][my] <= 0:
                break

            if 1 <= graph[mx][my]:
                value += graph[mx][my]
                cur_x, cur_y = mx, my


    if score < value:
        max_x, max_y = x, y
        score = value

def kill_tree(x,y):
    visited[x][y] = c
    graph[x][y] = 0
    for i in range(4):
        cur_x, cur_y = x, y
        for _ in range(k):
            nx, ny = x + ddx[i], y + ddy[i]
            
            if not (0 <= nx < n and 0 <= ny < n):
                break
            
            if graph[nx][ny] == -1:
                break
            
            if graph[nx][ny] == 0:
                visited[nx][ny] = c
                break

            if graph[nx][ny] > 0:
                visited[nx][ny] = c
                graph[nx][ny] = 0
                cur_x, cur_y = nx, ny

def remove_killer():
    for i in range(n):
        for j in range(n):
            if visited[i][j] > 0:
                visited[i][j] -= 1

for _ in range(m):
    grow()
    graph = seed()

    score = 0
    max_x, max_y = 0, 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                killer(i,j)
    
    remove_killer()

    kill_tree(max_x, max_y)
    

    answer += score
print(answer)