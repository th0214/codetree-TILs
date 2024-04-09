from collections import deque

N, M, K, C = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

k_graph = [[0] * N for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 0

def tree_grow():
    tmp = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                tmp.append((i,j))
    
    q = deque()
    for t_x, t_y in tmp:
        cnt = 0

        for k in range(4):
            nx, ny = t_x + dx[k], t_y + dy[k]
            if 0 <= nx < N and 0 <= ny <N and graph[nx][ny] > 0:
                cnt += 1
        
        graph[t_x][t_y] += cnt

def bunsik():
    tmp_graph = [[0] * N for _ in range(N)]
    tmp = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                tmp.append((i,j))
    
    for t_x, t_y in tmp:
        cnt = 0

        for k in range(4):
            nx, ny = t_x + dx[k], t_y + dy[k]
            if 0 <= nx < N and 0 <= ny <N and graph[nx][ny] == 0 and k_graph[nx][ny] == 0:
                cnt += 1
        
        if cnt > 0:
            for k in range(4):
                nx, ny = t_x + dx[k], t_y + dy[k]
                if 0 <= nx < N and 0 <= ny <N and graph[nx][ny] == 0 and k_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] += (graph[t_x][t_y] // cnt)
                

    for i in range(N):
        for j in range(N):
            if tmp_graph[i][j] > 0:
                graph[i][j] += tmp_graph[i][j]


def killer_select():
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]
    tmp_graph = [[0] * N for _ in range(N)]
    tmp = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                tmp.append((i,j))
    
    for x,y in tmp:
        cnt = 0
        for i in range(4):
            for j in range(1,K+1):
                nx, ny = x + dx[i] * j, y + dy[i] * j
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == -1 or graph[nx][ny] == 0:
                        break
                    else:
                        cnt += graph[nx][ny]

        tmp_graph[x][y] = cnt + graph[x][y]

    max_val = -1e9
    f_x, f_y = -1,-1
    for i in range(N):
        for j in range(N):
            if max_val < tmp_graph[i][j]:
                max_val = tmp_graph[i][j]
                f_x, f_y = i,j

    return f_x, f_y    


def kill(x,y):
    global answer
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]

    answer += graph[x][y]
    graph[x][y] = 0
    k_graph[x][y] = C+1

    for i in range(4):
        for j in range(1,K+1):
            nx, ny = x + dx[i] * j, y + dy[i] * j
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == -1 or graph[nx][ny] == 0:
                    k_graph[nx][ny] = C+1
                    break
                else:
                    answer += graph[nx][ny]
                    k_graph[nx][ny] = C+1
                    graph[nx][ny] = 0


def remove_killer():
    for i in range(N):
        for j in range(N):
            if k_graph[i][j] > 0:
                k_graph[i][j] -= 1
                
for _ in range(M):
    tree_grow()
    bunsik()
    x,y = killer_select()
    kill(x,y)
    remove_killer()

print(answer)