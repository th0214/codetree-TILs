from collections import deque

N, M, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

p_graph = [[[] for _ in range(N)] for _ in range(N)]

for i in range(1,M+1):
    x,y = map(int, input().split())
    p_graph[x-1][y-1].append(i)

f_x, f_y = map(int, input().split())
graph[f_x-1][f_y-1] = -1

exit = [f_x-1,f_y-1]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

p_life = [True] * (M+1)
total_move = 0

def distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def move(total):
    global total_move, p_graph
    tmp_graph = [[[] for _ in range(N)] for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if len(p_graph[i][j]):
                q.append((i,j))
    # if total == 1:
    #     print(q)
    while q:
        x,y = q.popleft()
        current_distance = distance(x,y,exit[0],exit[1])
    
        tmp = []
        for i in range(4):
            nx, ny = x+ dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                now = distance(nx,ny,exit[0],exit[1])
                if graph[nx][ny] == 0 and now < current_distance or graph[nx][ny] == -1:
                    tmp.append([nx,ny])

        if len(tmp):
            while len(p_graph[x][y]):
                p = p_graph[x][y].pop(0)
                # if total==1:
                #         print(p)
                if tmp[0][0] == exit[0] and tmp[0][1] == exit[1]:
                    p_life[p] = False
                else:
                    tmp_graph[tmp[0][0]][tmp[0][1]].append(p)
                    
                total_move += 1
        
    for i in range(N):
        for j in range(N):
            if len(tmp_graph[i][j]):
                while len(tmp_graph[i][j]):
                    p_graph[i][j].append(tmp_graph[i][j].pop(0))
        # if total == 1:
        #     print(p_graph)

def find_nemo(z):
    q = deque()

    for k in range(2,N+1):
        for i in range(0,N-k+1):
            for j in range(0,N-k+1):
                nx, ny = k+i-1,k+j-1
                
                if not (i <= exit[0] <= nx and j <= exit[1] <= ny):
                    continue
                
                alive = False
                for n in range(i,nx+1):
                    for m in range(j,ny+1): 
                        if len(p_graph[n][m]):
                            alive = True
                
                if alive == True:
                    return [k,i,j]
        

def rotate(z):
    global exit, graph, p_graph
    tmp = [[0] * N for _ in range(N)]
    tmp_person = [[[] for _ in range(N)] for _ in range(N)]
    k,s_x,s_y = find_nemo(z)

    
    for i in range(s_x, s_x+k):
        for j in range(s_y, s_y+k):
            o_x,o_y = i - s_x, j-s_y
            rx, ry = o_y, k-o_x-1

            if graph[i][j] > 0:
                tmp[rx+s_x][ry+s_y] = graph[i][j] -1
            else:
                tmp[rx+s_x][ry+s_y] = graph[i][j]
    
            tmp_person[rx+s_x][ry+s_y] = p_graph[i][j]
    
    for i in range(s_x, s_x+k):
        for j in range(s_y, s_y+k):
            graph[i][j] = tmp[i][j]
            p_graph[i][j] = tmp_person[i][j]
    
    # eixt 위치 찾기
    for i in range(s_x, s_x+k):
        for j in range(s_y, s_y+k):
            if graph[i][j] == -1:
                exit = [i,j]


for total in range(K):

    move(total)

    if any(p_life[1:]) == False:
        break

    # if total == 1:
    #     print(total_move, p_life)
    #     print(graph)
    #     print(p_graph)

    rotate(total)
    # if total == 1:
    #     print(total_move, p_life)
    #     print(graph)
    #     print(p_graph)

print(total_move)
print(exit[0]+1, exit[1]+1)