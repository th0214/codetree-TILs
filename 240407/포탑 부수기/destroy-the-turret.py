from collections import deque
N,M,K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
attack_life = [[0] * M for _ in range(N)]
p_pork = [[0] * M for _ in range(N)]
l_x = [0,1,0,-1]
l_y = [1,0,-1,0]

p_x = [0,-1,-1,-1,0,1,1,1]
p_y = [-1,-1,0,1,1,1,0,-1]

def choose_attack(now):
    tmp = []
    min_val = 1e9

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and min_val >= graph[i][j]:
                min_val = graph[i][j]
                tmp.append((graph[i][j],attack_life[i][j],i+j,i,j))
    
    tmp.sort(key=lambda x:(x[0],x[1],-x[2],-x[4]))
    attack_life[tmp[0][3]][tmp[0][4]] = now
    graph[tmp[0][3]][tmp[0][4]] += (N+M)

    return tmp[0][3], tmp[0][4]

def attack(a,b):
    tmp = []
    q = deque()
    q.append((a,b,[]))
    max_val = -1e9

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and (i,j) != (a,b) and max_val <= graph[i][j]:
                max_val = graph[i][j]
                tmp.append((graph[i][j],attack_life[i][j],i+j,i,j))

    tmp.sort(key=lambda x:(-x[0],x[1],x[2],x[4]))
    at_x, at_y = tmp[0][3], tmp[0][4]

    # 레이저 공격 or 포탄 공격

    can_lazer = False
    route = []
    route_length = 1e9
    visited = [[0] * M for _ in range(N)]
    visited[a][b] = 1

    while q:
        x,y,arr = q.popleft()

        for i in range(4):
            nx, ny = (x + l_x[i]) % N, (y + l_y[i]) % M

            if (nx,ny) == (at_x,at_y):
                if route_length > len(route):
                    route_length = len(route)
                    route.extend(arr)

            if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny,arr+[(nx,ny)]))
    
    if len(route):
        can_lazer = True
    
    if can_lazer:
        graph[at_x][at_y] -= graph[a][b]
        p_pork[at_x][at_y] = now

        for i,j in route:
            graph[i][j] -= (graph[a][b] // 2)
            p_pork[i][j] = now
    
    else:

        graph[at_x][at_y] -= graph[a][b]
        p_pork[at_x][at_y] = now

        for i in range(8):
            g_x, g_y = (at_x + p_x[i]) % N, (at_y + p_y[i]) % M

            if graph[g_x][g_y] > 0 and (g_x,g_y) != (a,b):
                graph[g_x][g_y] -= (graph[a][b] // 2)
                p_pork[g_x][g_y] = now

def check():
    for i in range(N):
        for j in range(M):
            if graph[i][j] <= 0:
                graph[i][j] = 0

def cure(now):
    for i in range(N):
        for j in range(M):
            if attack_life[i][j] < now and graph[i][j] > 0 and p_pork[i][j] < now:
                graph[i][j] += 1

def give_up():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                cnt += 1
    return cnt

for now in range(1,K+1):
    # print(graph)
    a_x, a_y = choose_attack(now)
    # print(graph)
    attack(a_x,a_y)
    # print(graph)
    check()
    cure(now)

    if give_up() == 1:
        break

result = -1e9

for i in graph:
    if result < max(i):
        result = max(i)

print(result)