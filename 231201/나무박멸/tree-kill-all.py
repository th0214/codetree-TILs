n, m, k, c = map(int, input().split())

graph = []
answer = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def grow():
    temp = []
    temp_blank = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                count = 0
                blank = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                        count += 1
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                        blank += 1
                temp.append([x, y, count])
                if blank > 0:
                    temp_blank.append([x, y, blank])

    for x, y, count in temp:
        graph[x][y] += count

    return temp_blank

def seed(tmp):
    for x,y,cnt in tmp:
            val = graph[x][y]//cnt
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and not visited[nx][ny]:
                    graph[nx][ny] += val

ddx = [-1,1,-1,1]
ddy = [1,1,-1,-1]
visited = [[0] * n for _ in range(n)]

def duk():
    global answer
    max_tree=0
    max_x,max_y = 0,0

    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                tree_sum = graph[x][y]
                for i in range(4):
                    for j in range(1,k+1):
                        nx, ny = x + (ddx[i] * j), y + (ddy[i] * j)
                        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 0 or graph[nx][ny] == -1:
                            break
                        tree_sum += graph[nx][ny]
                
                if tree_sum > max_tree:
                    max_tree = tree_sum
                    max_x, max_y = x,y
    
    if max_tree > 0:
        answer += max_tree
        graph[max_x][max_y] = 0
        for i in range(4):
            for j in range(1, k + 1):
                nx, ny = max_x + ddx[i] * j, max_y + ddy[i] * j
                if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 0:
                    break
                graph[nx][ny] = 0
    

for _ in range(m):
    tmp_blank = grow()
    seed(tmp_blank)
    duk()
   
print(answer)