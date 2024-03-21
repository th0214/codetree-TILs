dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

p_dx = [-1,0,1,0]
p_dy = [0,-1,0,1]
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
    position = []

    for i in range(4):
        for j in range(4):
            while graph[i][j][0]:
                nd = graph[i][j][0].pop()
                flag = False
                for _ in range(8):
                    nx = i + dx[nd]
                    ny = j + dy[nd]
                    if 0 <= nx < 4 and 0 <= ny < 4 and die[nx][ny] == 0 and not(nx == packman[0] and ny == packman[1]):
                        position.append((nx,ny,nd))
                        flag = True
                        break
                    
                    nd = (nd+1) % 8
                if flag == False:
                    position.append((i,j,nd))
    
    return position

def select_packman_move(x,y,cnt,eat,tmp):
    global max_fish_count, path

    if cnt == 3:
        if max_fish_count < eat:
            max_fish_count = eat
            path = tmp
        return

    for i in range(4):
        nx = x + p_dx[i]
        ny = y + p_dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                select_packman_move(nx,ny,cnt+1,eat+len(graph[nx][ny][0]),tmp+[i])
                visited[nx][ny] = False
            else:
                select_packman_move(nx,ny,cnt+1,eat, tmp+[i])

def move_packman(x,y):
    global die, packman

    for p in path:
        packman[0] = packman[0] + p_dx[p]
        packman[1] = packman[1] + p_dy[p]

        if graph[packman[0]][packman[1]][0] :
            graph[packman[0]][packman[1]][0] = []
            die[packman[0]][packman[1]] = 3


def reduce_die():
    global die
    for i in range(4):
        for j in range(4):
            if die[i][j] > 0:
                die[i][j] -= 1

def born():
    global graph
    for i in range(4):
        for j in range(4):
            while graph[i][j][1]:
                graph[i][j][0].append(graph[i][j][1].pop())

for _ in range(t):

    copy()
    tmp = move()
    for r,c,dir in tmp:
        graph[r][c][0].append(dir)
    
    path = []
    max_fish_count = -1

    select_packman_move(packman[0],packman[1],0,0,[])
    move_packman(packman[0],packman[1])
    
    reduce_die()
    born()
    

for i in range(4):
    for j in range(4):
            result += len(graph[i][j][0])

print(result)