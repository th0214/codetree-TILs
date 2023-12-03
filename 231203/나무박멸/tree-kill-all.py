n, m, k, c = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
answer = 0
visited = [[0] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ddx = [-1,1,-1,1]
ddy = [1,1,-1,-1]


def grow():
    tmp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                cnt = 0
                for a in range(4):
                    nx, ny = i + dx[a], j + dy[a]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                        tmp[i][j] += 1
    
    for i in range(n):
        for j in range(n):
            graph[i][j] += tmp[i][j]
                

def seed():
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                cnt = 0
                tmp_l = []
                for a in range(4):
                    nx, ny = i + dx[a], j + dy[a]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and visited[nx][ny] <= 0:
                        cnt += 1
                        tmp_l.append([nx,ny])
                if cnt > 0:
                    tmp_cnt = graph[i][j] // cnt
                    for b in tmp_l:
                        tmp[b[0]][b[1]] += tmp_cnt
    
    for i in range(n):
        for j in range(n):
            if tmp[i][j] > 0:
                graph[i][j] += tmp[i][j]

def killer(x,y):
    global score, max_x, max_y
    cnt = graph[x][y]
    for i in range(4):
        cur_x, cur_y = x, y
        for j in range(1, k+1):
            nx, ny = x + ddx[i] * j, y + ddy[i] * j
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == -1 or graph[nx][ny] == 0:
                    break
                elif graph[nx][ny] > 0:
                    cnt += graph[nx][ny]
                    cur_x, cur_y = nx, ny
            else:
                break
    if score < cnt:
        score = cnt
        max_x = x
        max_y = y

def kill_tree(x,y):
    visited[x][y] += c
    for i in range(4):
        for j in range(1, k+1):
            nx, ny = x + ddx[i] * j, y + ddy[i] * j
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == -1:
                    visited[nx][ny] += c
                    break
                elif graph[nx][ny] == 0:
                    visited[nx][ny] += c
                    graph[nx][ny] = 0
                    break
                elif graph[nx][ny] > 0:
                    visited[nx][ny] += c
                    graph[nx][ny] = 0

def remove_killer():
    for i in range(n):
        for j in range(n):
            if visited[i][j] > 0:
                visited[i][j] -= 1

for _ in range(m):
    grow()
    seed()
    score = 0
    max_x, max_y = 0, 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                killer(i,j)
    kill_tree(max_x, max_y)
    remove_killer()

    answer += score
print(answer)