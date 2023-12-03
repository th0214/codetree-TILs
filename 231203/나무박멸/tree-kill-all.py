from copy import deepcopy

n, m, k, c = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
answer = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ddx = [-1, 1, -1, 1]
ddy = [1, 1, -1, -1]

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
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and visited[nx][ny] <= 0:
                        cnt += 1
                if cnt != 0:
                    tmp_cnt = graph[i][j] // cnt
                    for a in range(4):
                        nx, ny = i + dx[a], j + dy[a]
                        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and visited[nx][ny] <= 0:
                            tmp[nx][ny] += tmp_cnt
    return tmp

def killer(x, y):
    global score, max_x, max_y
    cnt = graph[x][y]
    for i in range(4):
        cur_x, cur_y = x, y
        for j in range(k):
            nx, ny = cur_x + ddx[i], cur_y + ddy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                break
            if graph[nx][ny] <= 0:
                break
            if graph[nx][ny] > 0:
                cnt += graph[nx][ny]
                cur_x, cur_y = nx, ny
    if score < cnt:
        score = cnt
        max_x, max_y = x, y

def kill_tree(x, y):
    visited[x][y] += c
    graph[x][y] = 0
    for i in range(4):
        cur_x, cur_y = x, y
        for _ in range(k):
            nx, ny = cur_x + ddx[i], cur_y + ddy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                break
            if graph[nx][ny] == -1:
                break
            if graph[nx][ny] > 0:
                visited[nx][ny] += c
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
                killer(i, j)
    kill_tree(max_x, max_y)
    remove_killer()
    answer += score

print(answer)