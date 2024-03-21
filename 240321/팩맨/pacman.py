dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

m, t = map(int, input().split())

graph = [[[[],[]] for _ in range(4)] for _ in range(4)]
die = [[0 for _ in range(4)] for _ in range(4)]

x, y = map(int, input().split())
packman = [x-1,y-1]
visited = [[False] * 4 for _ in range(4)]
path = []

result = 0

for _ in range(m):
    x,y,d = map(int, input().split())
    graph[x-1][y-1][0].append(d-1)

def copy():

    for i in range(4):
        for j in range(4):
            for dir in graph[i][j][0]:
                graph[i][j][1].append(dir)


def move():
    tmp = [[[[],[]] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            for k in graph[i][j][0]:
                cnt = 0
                d = k
                while True:
                    ni = i + dx[d]
                    nj = j + dy[d]

                    if cnt == 8:
                        tmp[i][j][0] = graph[i][j][0]
                        break

                    if not (0 <= ni < 4 and 0 <= nj < 4) or die[ni][nj] > 0 or [ni, nj] == packman:
                        d = (d+1) % 8
                        cnt += 1
                    else:
                        tmp[ni][nj][0].append(d)
                        break
    
    for i in range(4):
        for j in range(4):
            graph[i][j][0] = tmp[i][j][0]

def select_packman_move(x,y,cnt,eat,tmp):
    global max_fish_count, path

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    if cnt == 3:
        if max_fish_count < eat:
            max_fish_count = eat
            path = tmp
        return

        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                select_packman_move(nx,ny,cnt+1,eat+len(graph[nx][ny][0]),tmp+[i])
                visited[nx][ny] = False
            else:
                select_packman_move(nx,ny,cnt+1,eat, tmp+[i])

def move_packman(x,y):
    global die, packman
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    for p in path:
        nx = x + dx[p]
        ny = y + dy[p]

        if 0 <= nx < 4 and 0 <= ny < 4:
            if len(graph[nx][ny][0]) > 0:
                graph[nx][ny][0] = []
                die[nx][ny] = 3
        x,y = nx,ny
    
    packman = [nx, ny]

def reduce_die():

    for i in range(4):
        for j in range(4):
            if die[i][j] > 0:
                die[i][j] -= 1

def born():
    tmp = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            if len(graph[i][j][1]) > 0:
                for k in graph[i][j][1]:
                    tmp[i][j].append(k)
                graph[i][j][1] = []
    
    for i in range(4):
        for j in range(4):
            if len(tmp[i][j]) > 0:
                for k in tmp[i][j]:
                    graph[i][j][0].append(k)

for _ in range(t):

    copy()
    move()
    max_fish_count = -1
    select_packman_move(packman[0],packman[1],0,0,[])
    move_packman(packman[0],packman[1])
    
    reduce_die()
    born()

for i in range(4):
    for j in range(4):
            result += len(graph[i][j][0])

print(result)