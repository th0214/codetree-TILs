from collections import deque

M, T = map(int, input().split())

p_x, p_y = map(int, input().split())
p_l = [p_x-1,p_y-1]

m_dx = [-1,-1,0,1,1,1,0,-1]
m_dy = [0,-1,-1,-1,0,1,1,1]

p_dx = [-1,0,1,0]
p_dy = [0,-1,0,1]

graph = [[[[],[]] for _ in range(4)] for _ in range(4)]
die_graph = [[0] * 4 for _ in range(4)]

for _ in range(M):
    x,y,d = map(int, input().split())
    graph[x-1][y-1][0].append(d-1)

def copy():

    for i in range(4):
        for j in range(4):
            if len(graph[i][j][0]) > 0:
                for k in graph[i][j][0]:
                    graph[i][j][1].append(k)

def m_move():
    tmp = []
    tmp_graph = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            if len(graph[i][j]) > 0:
                tmp.append((i,j))
    
    for x,y in tmp:

        while len(graph[x][y][0]):
            nd = graph[x][y][0].pop()
            flag = False
            for _ in range(8):
                nx = x + m_dx[nd]
                ny = y + m_dy[nd]
                if 0 <= nx < 4 and 0 <= ny < 4 and die_graph[nx][ny] == 0 and not(nx == p_l[0] and ny == p_l[1]):
                    tmp_graph[nx][ny].append(nd)
                    flag = True
                    break
                
                nd = (nd+1) % 8
            if flag == False:
                tmp_graph[x][y].append(nd)

    for i in range(4):
        for j in range(4):
            if len(tmp_graph[i][j]):
                while len(tmp_graph[i][j]):
                    graph[i][j][0].append(tmp_graph[i][j].pop(0))



def p_move(x,y,cnt,arr,catch):
    global max_catch, route

    if cnt == 3:
        if catch > max_catch:
            route = arr
            max_catch = catch
        return

    for i in range(4):
        nx, ny = x + p_dx[i], y + p_dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                p_move(nx,ny,cnt+1,arr+[(nx,ny)],catch+len(graph[nx][ny][0]))
                visited[nx][ny] = False
            else:
                p_move(nx,ny,cnt+1,arr+[(nx,ny)],catch)

def eat(route):
    global p_l
    # 몬스터 잡아 먹기
    for x,y in route:
        if len(graph[x][y][0]):
            graph[x][y][0] = []
            die_graph[x][y] = 3
    
    p_l = [route[-1][0], route[-1][1]]

def discount():
    for i in range(4):
        for j in range(4):
            if die_graph[i][j] > 0:
                die_graph[i][j] -= 1

def born():

    for i in range(4):
        for j in range(4):
            if len(graph[i][j][1]):
                while len(graph[i][j][1]):
                    graph[i][j][0].append(graph[i][j][1].pop())
            
for t in range(T):
    copy()
    # if t == 1:
    #     print(graph)
    m_move()
    # if t == 1:
    #     print(graph)

    visited = [[0] * 4 for _ in range(4)]
    route = []
    max_catch = -1e9

    p_move(p_l[0],p_l[1],0,[],0)
    eat(route)
    # if t == 1:
    #     print(graph)
    discount()
    born()

answer = 0

for i in range(4):
    for j in range(4):
        if len(graph[i][j][0]):
            answer += len(graph[i][j][0])

print(answer)