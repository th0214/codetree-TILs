from collections import deque

N, M, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
attack_graph = [[0] * M for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
t = 1

def select_attack():
    max_num = 5001
    a_x = a_y = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                continue
            if graph[i][j] < max_num:
                max_num = graph[i][j]
                a_x, a_y = i, j
            elif graph[i][j] == max_num:
                if attack_graph[i][j] > attack_graph[a_x][a_y]:
                    a_x, a_y = i, j
                elif attack_graph[i][j] == attack_graph[a_x][a_y]:
                    if i+j > a_x + a_y:
                       a_x, a_y = i,j
                    elif i+j == a_x + a_y:
                        if j > a_y:
                            a_x, a_y = i, j
    return a_x, a_y
                         
def select_target():
    min_num = -1
    t_x = t_y = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            if graph[i][j] > min_num:
                min_num = graph[i][j]
                t_x, t_y = i, j
            elif graph[i][j] == min_num:
                if attack_graph[i][j] < attack_graph[t_x][t_y]:
                    t_x, t_y == i, j
                elif attack_graph[i][j] == attack_graph[t_x][t_y]:
                    if i+j < t_x + t_y:
                        t_x, t_y = i, j
                    elif i+j == t_x+t_y:
                        if j < t_y:
                            t_x, t_y = i, j
    return t_x, t_y 
            
def lazer(a_x, a_y, t_x, t_y):
    visited = [[False] * M for _ in range(N)]
    q = deque()
    visited[a_x][a_y] = True
    q.append((a_x,a_y,[]))
    while q:
        x, y, path = q.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]) % N, (y + dy[i]) % M
            if visited[nx][ny] == True:
                continue
            if graph[nx][ny] == 0:
                continue
            
            if nx == t_x and ny == t_y:
                graph[nx][ny] -= point
                for rx, ry in path:
                    graph[rx][ry] -= half_point
                    attack[rx][ry] = True
                return True

            tmp_path = path[:]
            tmp_path.append((nx,ny))
            visited[nx][ny] = True
            q.append((nx,ny,tmp_path))
    return False

def bomb(a_x, a_y, t_x, t_y):
    graph[t_x][t_y] -= point
    ddx = dx + [1,1,-1,-1]
    ddy = dy + [1,-1,-1,1]

    for i in range(8):
        nx = (t_x + ddx[i]) % N
        ny = (t_y + ddy[i]) % M
        attack[nx][ny] = True
        if a_x == t_x and a_y == t_y:
            continue
        graph[nx][ny] -= half_point

def check_crush():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                continue
            if graph[i][j] < 0:
                graph[i][j] = 0

def max_check():
    return max([max(line) for line in graph])

def fix_tarret():
    tarret_num = 0
    turret = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            tarret_num += 1
            if attack[i][j]:
                continue
            turret.append((i,j))

    if tarret_num == 1:
        print(max_check())
        exit(0)
    for x,y in turret:
        graph[x][y] += 1

for k in range(K):
    attack = [[False] * M for _ in range(N)]

    #공격자 선정
    a_x, a_y = select_attack()
    graph[a_x][a_y] += N+M
    point = graph[a_x][a_y]
    half_point = point//2
    attack[a_x][a_y] = True
    attack_graph[a_x][a_y] += t
    t += 1
    
    #공격자의 공격
    t_x, t_y = select_target()
    attack[t_x][t_y] = True

    if not lazer(a_x, a_y, t_x, t_y):
        bomb(a_x, a_y, t_x, t_y)
    
    #포탑 부셔짐
    check_crush()

    #포탑 정비
    fix_tarret()

print(max_check())