n, m, k, c = map(int, input().split())

graph = []
answer = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def grow():
    tmp = []
    tmp_blank = []
    for i, num in enumerate(graph):
        for j, num2 in enumerate(num):
            if num2 > 0:
                cnt = 0
                blank_cnt = 0
                for k in range(4):
                    if 0 <= i+dx[k] < n and 0 <= j+dy[k] < n and graph[i+dx[k]][j+dy[k]] > 0:
                        cnt += 1
                    if 0 <= i+dx[k] < n and 0 <= j+dy[k] < n and graph[i+dx[k]][j+dy[k]] == 0 and not visited[i+dx[k]][j+dy[k]]:
                        blank_cnt += 1
                tmp.append([i,j,cnt])  
                tmp_blank.append([i,j, blank_cnt])
    for x,y, count in tmp:
        graph[x][y] += count

    return tmp_blank

def seed(tmp):
    tmp_graph = []
    for x,y,cnt in tmp:
        if cnt > 0:
            val = graph[x][y]//cnt
            for k in range(4):
                if 0 <= x+dx[k] < n and 0 <= y+dy[k] < n and graph[x+dx[k]][y+dy[k]] == 0 and not visited[x+dx[k]][y+dy[k]]:
                    tmp_graph.append([x+dx[k],y+dy[k],val])
                
    
    for x,y,val in tmp_graph:
        graph[x][y] += val

ddx = [-1,1,-1,1]
ddy = [1,1,-1,-1]
visited = [[0] * n for _ in range(n)]

def duk(x,y):
    global total, visited
    t_list = [[0] * n for _ in range(n)]
    standard = graph[x][y]
    t_list[x][y] = c
    for i in range(4):
        for j in range(1,k+1):
            nx, ny = x + (ddx[i] * j), y + (ddy[i] * j)
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                standard += graph[nx][ny]
                t_list[nx][ny] = c
            elif 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                t_list[nx][ny] = c
                break
            elif 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == -1:
                break
                
    if total < standard:
        total = standard
        visited = t_list.copy()
    

def duk_remove(visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] > 0:
                visited[i][j] -= 1
                graph[i][j] = 0

for _ in range(m):
    tmp_blank = grow()
    seed(tmp_blank)

    total = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                duk(i,j)
                
    duk_remove(visited)
    answer += total
print(answer)