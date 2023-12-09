from collections import deque

N, M, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
graph_attack = [[0] * M for _ in range(N)]
time = 1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def attack_check():
    power = 5001
    ax = ay = 0 
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            if graph[i][j] < power:
                power = graph[i][j]
                ax,ay = i, j
            elif graph[i][j] == power:
                if graph_attack[i][j] > graph_attack[ax][ay]:
                    ax, ay = i, j
                elif graph_attack[i][j] == graph_attack[ax][ay]:
                    if i + j > ax + ay:
                        ax, ay = i, j
                    elif i + j == ax + ay:
                        if j > ay:
                            ay = y
    return ax, ay

def target_check(a_i, a_j):
    power = -1
    tx = ty = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            if i == a_i and j == a_j:
                continue
            if graph[i][j] > power:
                power = graph[i][j]
                tx, ty = i, j
            elif graph[i][j] == power:
                if graph_attack[i][j] < graph_attack[tx][ty]:
                    tx, ty = i, j
                elif graph_attack[i][j] == graph_attack[tx][ty]:
                    if i+j < tx+ty:
                        tx,ty = i,j
                    elif i+j == tx+ty:
                        if j < ty:
                            tx, ty = i, j
    return tx, ty

def laser(ax, ay, tx, ty):
    q = deque()
    q.append((ax,ay,[]))
    visited = [[False] * M for _ in range(N)]
    visited[ax][ay] = True
    while q:
        x,y, route = q.popleft()
        for i in range(4):
            nx = (x + dx[i]) % N
            ny = (y + dy[i]) % M
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 0:
                continue
            
            if nx == tx and ny == ty:
                graph[nx][ny] -= point
                for rx, ry in route:
                    graph[rx][ry] -= half_point
                    attack[rx][ry] = True
                return True
            
            tmp_route = route[:]
            tmp_route.append((nx,ny))
            visited[nx][ny] = True
            q.append((nx,ny,tmp_route))

    return False

def shell(ax, ay, tx, ty):
    graph[tx][ty] -= point
    ddx = dx + [1,1,-1,-1]
    ddy = dy + [-1,1,-1,1]

    for d in range(8):
        nx = (tx + ddx[d]) % N
        ny = (ty + ddy[d]) % M
        if ax == nx and ay == ny:
            continue
        graph[nx][ny] -= half_point
        attack[nx][ny] = True

def break_check():
    for i in range(N):
        for j in range(M):
            if graph[i][j] < 0:
                graph[i][j] = 0

def max_check():
    return max([max(line) for line in graph])

def turret_check():
    turret = []
    turret_cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            turret_cnt += 1
            if attack[i][j]:
                continue
            turret.append((i,j))
    
    if turret_cnt == 1:
        print(max_check())
        exit(0)
    for x,y in turret:
        graph[x][y] += 1
            
            
for k in range(K):
    attack = [[False] * M for _ in range(N)]

    # 공격자 선정
    attack_i, attack_j = attack_check()
    graph[attack_i][attack_j] += N + M
    point = graph[attack_i][attack_j]
    half_point = point // 2
    attack[attack_i][attack_j] = True
    graph_attack[attack_i][attack_j] = time
    time += 1

    # 공격자 공격
    target_i, target_j = target_check(attack_i, attack_j)
    attack[target_i][target_j] = True

    if not laser(attack_i, attack_j, target_i, target_j):
        shell(attack_i, attack_j, target_i, target_j)
    
    # 포탑 부셔짐 체크
    break_check()

    #포탑 정비
    turret_check()

print(max_check())