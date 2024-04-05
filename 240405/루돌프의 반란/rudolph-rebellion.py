from collections import deque

N, M, P, C, D = map(int, input().split())

graph = [[[0,0] for _ in range(N)] for _ in range(N)]
santa_score = [0] * (P+1)
santa_life = [True] * (P+1)
santa_stern = [0] * (P+1)


L_r, L_c = map(int, input().split())
graph[L_r-1][L_c-1] = [0,1]

L_dx = [0,-1,-1,-1,0,1,1,1]
L_dy = [-1,-1,0,1,1,1,0,-1]
S_dx = [-1,0,1,0]
S_dy = [0,1,0,-1]

for _ in range(P):
    num, s_r, s_c = map(int, input().split())

    graph[s_r-1][s_c-1] = [num,2]

def L_move(graph):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    tmp = []
    for i in range(N):
        for j in range(N):
            if graph[i][j][1] == 1:
                q.append((i,j))
                
    x,y = q.popleft()

    for i in range(N):
        for j in range(N):
            if graph[i][j][1] == 2:
                visited[i][j] = (x-i)**2 + (y-j)**2
     
    # 가장 가까운 산타 찾기    
    max_num = 1e9

    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0 and visited[i][j] <= max_num:
                max_num = visited[i][j]
                tmp = [i,j]
    
    # 루돌프 최종 이동
    check = []
    m_num = 1e9
    for i in range(8):
        nx, ny = x + L_dx[i], y + L_dy[i]
        if 0 <= nx < N and 0 <= ny <N:
            num = abs(tmp[0]-nx) + abs(tmp[1]-ny)

            if num <= m_num:
                m_num = num
                check = [nx,ny,i]

    if graph[check[0]][check[1]][1] == 2:
        santa_score[graph[check[0]][check[1]][0]] += C
        tmp = [graph[check[0]][check[1]][0]]
        graph[x][y], graph[check[0]][check[1]] = [0,0], graph[x][y]

        deer_splash(check[0],check[1],check[2],tmp[0],C)

        if santa_life[tmp[0]] == True:
            santa_stern[tmp[0]] = 2
        

    if graph[check[0]][check[1]][1] == 0:
        graph[x][y], graph[check[0]][check[1]] = graph[check[0]][check[1]], graph[x][y]

    return check[0], check[1]

def S_move(num,L_x,L_y):
    q = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] == num and santa_life[num] == True:
                q.append((i,j))
            
    if len(q):
        x,y = q.popleft()
        cur_distance = (x-L_x)**2 + (y-L_y)**2
        check = []

        for i in range(4):
            nx,ny = x + S_dx[i], y+S_dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                length = (L_x-nx)**2 + (L_y-ny)**2

                if length < cur_distance:
                    check.append([length,nx,ny,i])

        check.sort(key=lambda x:(x[0],x[3]))

        if len(check):
            f_x, f_y, d = check[0][1],check[0][2], check[0][3]
            
            if graph[f_x][f_y][1] == 2:
                if len(check) > 1:
                    for i in range(1,len(check)):
                        if graph[check[i][1]][check[i][2]] != 2:
                            f_x, f_y,d = check[i][1], check[i][2],check[i][3]
                            break
                        else:
                            f_x, f_y = x,y
                else:
                    f_x, f_y = x,y

        else:
            f_x,f_y = x,y

        # 만약 루돌프가 있다면

        if graph[f_x][f_y][1] == 1:
            graph[x][y] = [0,0]
            santa_score[num] += D
            santa_stern[num] += 2
            d = (d+2)%4
            # 산타가 범위 밖으로 튕긴다
            santa_splash(f_x,f_y,num,d,D)

        else:
            # print(f_x,f_y,x,y)
            graph[f_x][f_y], graph[x][y] = graph[x][y], graph[f_x][f_y]

def santa_splash(x,y,num,d,length):

    new_x, new_y = x + S_dx[d] * length, y + S_dy[d] * length

    if not (0 <= new_x < N and 0 <= new_y < N):
                santa_life[num] = False
                return
    else:
        if graph[new_x][new_y][1] == 2:
            tmp = [graph[new_x][new_y][0], graph[new_x][new_y][1]]
            graph[new_x][new_y] = [num, 2]
            santa_splash(new_x,new_y,tmp[0],d,1)
        else:
            graph[new_x][new_y] = [num,2]

def deer_splash(x,y,d,num,length):

    new_x, new_y = x + L_dx[d] * length, y + L_dy[d]*length

    if not (0 <= new_x < N and 0 <= new_y < N):
            santa_life[num] = False
            return
    else:
        if graph[new_x][new_y][1] == 2:
            tmp = [graph[new_x][new_y][0], graph[new_x][new_y][1]]
            graph[new_x][new_y] = [num, 2]
            santa_splash(new_x,new_y,tmp[0],d,1)
        else:
            graph[new_x][new_y] = [num,2]




for _ in range(M):
    L_x, L_y = L_move(graph)
    # print(santa_life, santa_stern)
    
    for i in range(1, P+1):
        if santa_life[i] == True and santa_stern[i] == 0:
            S_move(i, L_x, L_y)
    
    for i in range(1, P+1):
        if santa_life[i] == True:
            santa_score[i] += 1

    if any(santa_life[1:]) == False:
        break
    
    for i in range(1, P+1):
        if santa_stern[i] > 0:
            santa_stern[i] -= 1

print(' '.join(map(str,santa_score[1:])))