from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
score = 0
def comb(x,y,graph,visited):

    check = [[x,y]]
    red = []

    visited[x][y] = 1
    color = graph[x][y]
    

    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == color:
                    check.append([nx,ny])
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    red.append([nx,ny])
                    q.append((nx,ny))
    

    for x,y in red:
        visited[x][y] = 0
    
    return [len(check+red), len(red), check+red]


def delete(l):
    global score

    score += l[0][0] ** 2

    for x, y in l[0][2]:
        graph[x][y] = -2
    

def move(graph):
    for i in range(n-2, -1, -1):
        for j in range(n):
            if graph[i][j] != -1:
                standard = i

                while standard+1 < n and graph[standard+1][j] == -2:
                    graph[standard+1][j] = graph[standard][j]
                    graph[standard][j] = -2
                    standard += 1

def rotate90(graph):
    tmp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            tmp[n-j-1][i] = graph[i][j]
    
    return tmp


while True:
    tmp = []
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1 and visited[i][j] == 0:
                check = comb(i,j,graph,visited)
                if check[0] >= 2:
                    tmp.append(check)

    def sort_condition(x):
        max_row = max(x[2], key=lambda item: item[0])[0]  # 행이 가장 큰 값
        min_col = min(x[2], key=lambda item: item[1])[1]  # 열이 가장 작은 값
        return (-x[0], x[1], -max_row, min_col)

    tmp.sort(key=sort_condition)

    if len(tmp) == 0:
        break

    delete(tmp)
    move(graph)
    graph = rotate90(graph)
    move(graph)
    
print(score)