n, m, k, c = map(int, input().split())

graph = []
answer = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def grow():
    tmp_blank = []
    for i, num in enumerate(graph):
        for j, num2 in enumerate(num):
            if num2 > 0:
                cnt = 0
                blank_cnt = 0
                for k in range(4):
                    if 0 <= i+dx[k] < n and 0 <= j+dy[k] < n and graph[i+dx[k]][j+dy[k]] > 0 and not visited[i+dx[k]][j+dy[k]]:
                        cnt += 1
                    if 0 <= i+dx[k] < n and 0 <= j+dy[k] < n and graph[i+dx[k]][j+dy[k]] == 0 and not visited[i+dx[k]][j+dy[k]]:
                        blank_cnt += 1
                        
                tmp_blank.append([i,j, blank_cnt])
                graph[i][j] = graph[i][j] + cnt
    return tmp_blank

def seed(tmp):
    tmp_graph = [[0] * n for _ in range(n)]
    for x,y,cnt in tmp:
        for k in range(4):
            if 0 <= x+dx[k] < n and 0 <= y+dy[k] < n and graph[x+dx[k]][y+dy[k]] == 0 and not visited[x+dx[k]][y+dy[k]]:
                tmp_graph[x+dx[k]][y+dy[k]] += graph[x][y] // cnt
    
    for i in range(n):
        for j in range(n):
            graph[i][j] += tmp_graph[i][j]

ddx = [-1,1,-1,1]
ddy = [1,1,-1,-1]

def duk(x,y):
    global total, visited
    t_sum = 0
    t_list = [[0] * n for _ in range(n)]
    for i in range(4):
        for j in range(1,k+1):
            nx, ny = x + (ddx[i] * j), y + (ddy[i] * j)
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                t_sum += graph[nx][ny]
                t_list[nx][ny] = c
            elif 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                t_list[nx][ny] = c
                break
            else:
                break
                
    if total < t_sum + graph[x][y]:
        total = t_sum + graph[x][y]
        t_list[x][y] = c
        visited = t_list

visited = [[0] * n for _ in range(n)]

def remove():
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j] > 0:
                graph[i][j] = 0

def duk_remove():
    global visited
    for i in range(n):
        for j in range(n):
            if visited[i][j] > 0:
                visited[i][j] -= 1

for _ in range(m):
    tmp_blank = grow()
    seed(tmp_blank)
    total = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                duk(i,j)
    answer += total
    remove()
    duk_remove()

print(answer)