from collections import deque
N, M, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

l_x = [0,1,0,-1]
l_y = [1,0,-1,0]

pok_x = [0,-1,-1,-1,0,1,1,1]
pok_y = [-1,-1,0,1,1,1,0,-1]
attack_exper = [[0] * M for _ in range(N)]
# print(graph)

def attacker_c(now):
    min_val = 1e9

    tmp = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] <= min_val and graph[i][j] !=0:
                min_val = graph[i][j]
                tmp.append((i,j, i+j, attack_exper[i][j], graph[i][j]))
    
    tmp.sort(key=lambda x: (x[4],-x[3],-x[2],-x[1]))
    attack_exper[tmp[0][0]][tmp[0][1]] = now
    graph[tmp[0][0]][tmp[0][1]] += (N+M)

    return tmp[0][0], tmp[0][1]


def attack(a,b,now):
    q = deque()
    q.append((a,b,[]))
    max_val = -1e9
    
    tmp = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and (i,j) != (a,b) and graph[i][j] >= max_val:
                    max_val = graph[i][j]
                    tmp.append((i,j, i+j, attack_exper[i][j], graph[i][j]))
    
    if len(tmp):
        tmp.sort(key=lambda x:(-x[4],x[3],x[2],x[1]))
        a_x, a_y = tmp[0][0], tmp[0][1]

        lazer_attack = False
        route = []
        route_length = 1e9
        visited = [[0] * M for _ in range(N)]
        visited[a][b] = 1

        while q:
            x,y,arr = q.popleft()

            if x == a_x and y == a_y:
                if route_length > len(arr):
                    route_length = len(arr)
                    route.extend(arr)

            for i in range(4):
                nx, ny = (x + l_x[i]) % N, (y + l_y[i]) % M

                if visited[nx][ny] == 0 and graph[nx][ny] > 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny,arr+[(nx,ny)]))
        
    
        if len(route):
            lazer_attack = True
        
        if lazer_attack:
            for x,y in route:
                if x == a_x and y == a_y:
                    graph[x][y] -= graph[a][b]
                    attack_exper[x][y] = now
                else:
                    graph[x][y] -= graph[a][b] // 2
                    attack_exper[x][y] = now
        else:

            graph[a_x][a_y] -= graph[a][b]
            attack_exper[a_x][a_y] = now
            for i in range(8):
                nx, ny = (a_x + pok_x[i])%N, (a_y + pok_y[i])%M

                if graph[nx][ny] > 0 and (nx, ny) != (a,b):
                    graph[nx][ny] -= (graph[a][b] // 2)
                    attack_exper[nx][ny] = now

def check_zero():
    for i in range(N):
        for j in range(M):
            if graph[i][j] <= 0:
                graph[i][j] = 0

def cure(now):
    for i in range(N):
        for j in range(M):
            if attack_exper[i][j] < now and graph[i][j] != 0:
                graph[i][j] += 1


for now in range(1,K+1):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                cnt += 1
    
    if cnt == 1:
        break

    x,y = attacker_c(now)
    # if now == 1:
    #     print(graph)
    attack(x,y, now)
    # if now == 1:
    #     print(graph)
    check_zero()
    cure(now)
    # if now == 1:
    #     print(graph)
    
result = 0

for i in graph:
    if result < max(i):
        result = max(i)
print(result)