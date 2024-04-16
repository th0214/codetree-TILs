from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C, K = map(int, input().split())
result = 0
graph = [[0] * C for _ in range(R+3)]

def setting(c, d):
    for i in range(R+1,0,-1):
        if graph[i+1][c] == graph[i][c-1] == graph[i][c+1] == 0:
            state, tmp = check_left(i,c,d)
            if state == True:
                return tmp

            state1, tmp1 = check_right(i,c,d)
            if state1 == True:
                return tmp1

            return [i,c,d]

def check_left(i,c,d):
    x, y = i, c
    # print(x,y)
    for k in range(C-c+1,0,-1):
        y = y-k
        if 0 <= y-1:
            if graph[x][y-1] == graph[x-1][y] == graph[x][y+1] == graph[x+1][y] == 0:
                x = x + k
                if x + 1 < R + 3:
                    if graph[x][y - 1] == graph[x - 1][y] == graph[x][y + 1] == graph[x + 1][y] == 0:
                        for l in range(R-x+1,-1,-1):
                            x = x+l
                            # print(x)
                            if graph[x][y - 1] == graph[x - 1][y] == graph[x][y + 1] == graph[x + 1][y] == 0:
                                return True, [x,y,(d-k)%4]
                            else:
                                x = x-l
                                continue
                    else:
                        x, y = i, c
                        continue
                else:
                    x, y = i, c
                    continue
            else:
                x, y = i, c
                continue
        else:
            x, y = i, c
            continue

    return False, [x, y, d]

def check_right(i,c,d):
    x,y = i,c
    for k in range(C-c+1,0,-1):
        y = y + k

        if y+1 < C:
            if graph[x][y-1] == graph[x-1][y] == graph[x][y+1] == graph[x+1][y] == 0:
                x = x + k
                if x+1 < R+3:
                    if graph[x][y - 1] == graph[x - 1][y] == graph[x][y + 1] == graph[x + 1][y] == 0:
                        for l in range(R - x + 1, -1, -1):
                            x = x + l
                            if graph[x][y - 1] == graph[x - 1][y] == graph[x][y + 1] == graph[x + 1][y] == 0:
                                return True, [x, y, (d +k) % 4]
                            else:
                                x = x - l
                                continue
                    else:
                        x, y = i, c
                        continue
                else:
                    x, y = i, c
                    continue
            else:
                x,y = i,c
                continue
        else:
            x, y = i, c
            continue

    return False, [x,y,d]

def draw(i,j,d):
    global graph
    if i-1 < 3:
        graph = [[0] * C for _ in range(R+3)]

    else:
        if d == 0:
            graph[i][j] = graph[i][j-1] = graph[i+1][j] = graph[i][j+1] = 1
            graph[i-1][j] = -1
        elif d == 1:
            graph[i][j] = graph[i][j - 1] = graph[i + 1][j] = graph[i - 1][j] = 1
            graph[i][j + 1] = -1
        elif d == 2:
            graph[i][j] = graph[i][j - 1] = graph[i][j+1] = graph[i - 1][j] = 1
            graph[i+1][j] = -1
        else:
            graph[i][j] = graph[i+1][j] = graph[i][j + 1] = graph[i - 1][j] = 1
            graph[i][j-1] = -1

def move(i,j,d):
    global result
    q =deque()
    q.append((i,j,0))
    max_depth = -100
    visited = [[0] * C for _ in range(R+3)]
    visited[i][j] = 1

    while q:
        x,y,check = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R+3 and 0 <= ny < C:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if check == 1:
                        q.append((nx,ny,1))
                    if max_depth < nx:
                        max_depth = nx
                elif graph[nx][ny] == -1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny,1))
                    if max_depth < nx:
                        max_depth = nx
    result += max_depth-2


for _ in range(K):
    c, d = map(int, input().split())

    i,j,d = setting(c-1, d)
    draw(i,j,d)
    if i - 1 >= 3:
        move(i,j,d)

print(result)