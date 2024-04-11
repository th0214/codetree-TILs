from collections import deque

N,M,P,C,D = map(int, input().split())

l_x, l_y = map(int, input().split())

l_l = [l_x-1,l_y-1]

graph = [[0] * N for _ in range(N)]
santa_l = [[0]]

for _ in range(P):
    idx, r, c = map(int, input().split())
    graph[r-1][c-1] = idx
    santa_l.append([r-1,c-1])

l_dx = [0,-1,-1,-1,0,1,1,1]
l_dy = [-1,-1,0,1,1,1,0,-1]

s_dx = [-1,0,1,0]
s_dy = [0,1,0,-1]

santa_life = [True] * (P+1)
santa_score = [0] * (P+1)
santa_stun = [0] * (P+1)

def distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

def l_move(t):
    global l_l

    tmp = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                tmp.append((i,j,distance(i,j,l_l[0],l_l[1])))

    tmp.sort(key=lambda x:(x[2],-x[0],-x[1]))

    min_num = 1e9
    check = []
    for i in range(8):
            nx, ny = l_l[0] + l_dx[i], l_l[1] + l_dy[i]

            if 0 <= nx < N and 0 <= ny < N and distance(nx,ny,tmp[0][0],tmp[0][1]) < min_num:
                if len(check):
                    check.pop()
                    check.append((nx,ny,i))
                    min_num = distance(nx,ny,tmp[0][0],tmp[0][1])
                else:
                    check.append((nx,ny,i))
                    min_num = distance(nx,ny,tmp[0][0],tmp[0][1])
    
    l_l = [check[0][0],check[0][1]]
    
    if graph[check[0][0]][check[0][1]] > 0:
        santa_score[graph[check[0][0]][check[0][1]]] += C
        santa_stun[graph[check[0][0]][check[0][1]]] = 2
        l_crush(check[0][0],check[0][1],check[0][2],C,graph[check[0][0]][check[0][1]])

def l_crush(x,y,direction,length,idx):

    nx, ny = x + l_dx[direction] *length, y + l_dy[direction] * length

    if not (0<=nx<N and 0<=ny<N):
        santa_life[idx] = False
        graph[x][y] = 0
        return
    
    if 0 <= nx < N and 0 <= ny < N:
        if graph[nx][ny] == 0:
            graph[x][y], graph[nx][ny] = 0, idx
            santa_l[idx] = [nx,ny]
        else:
            tmp = graph[nx][ny]
            santa_l[idx] = [nx,ny]
            graph[x][y], graph[nx][ny] = 0, idx
            l_crush(nx,ny,tmp,direction,1)

def s_move(t):

    for santa in range(1,P+1):

        if santa_life[santa] == True and santa_stun[santa] == 0:
            tmp = []
            x,y = santa_l[santa]
            min_num = 1e9
            current_distance = distance(x,y,l_l[0],l_l[1])
            for i in range(4):
                nx, ny = x + s_dx[i], y + s_dy[i]

                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                    if distance(l_l[0],l_l[1],nx,ny) < min_num and distance(l_l[0],l_l[1],nx,ny) < distance(x,y,l_l[0],l_l[1]):
                        if len(tmp):
                            tmp.pop()
                            min_num = distance(l_l[0],l_l[1],nx,ny)
                            tmp.append((nx,ny,min_num,i))
                        else:
                            min_num = distance(l_l[0],l_l[1],nx,ny)
                            tmp.append((nx,ny,min_num,i))
            
            if len(tmp):
                f_x, f_y, direction = tmp[0][0], tmp[0][1], tmp[0][3]

                if (f_x,f_y) != (l_l[0],l_l[1]):
                    graph[x][y], graph[f_x][f_y] = graph[f_x][f_y], graph[x][y]
                    santa_l[santa] = [f_x,f_y]

                else:
                    santa_score[santa] += D
                    direction = (direction+2) % 4
                    santa_stun[santa] = 2
                    santa_crush(f_x,f_y,santa,direction,D)
                    graph[x][y] = 0
            
def santa_crush(x,y,idx,direction,length):

    nx, ny = x + s_dx[direction] * length, y + s_dy[direction] * length
    
    if not (0 <= nx < N and 0 <= ny < N):
        santa_life[idx] = False
        santa_l[idx] = [0,0]
        return
    
    if 0 <= nx < N and 0 <= ny < N:
        if graph[nx][ny] == 0:
            graph[nx][ny] = idx
            santa_l[idx] = [nx,ny]
        else:
            tmp = graph[nx][ny]
            santa_l[idx] = [nx,ny]
            graph[nx][ny] = idx
            santa_crush(nx,ny,tmp,direction,1)
        

def plus_one():
    for i in range(1,P+1):
        if santa_life[i] == True:
            santa_score[i] += 1

def stun_minus():
    for i in range(1,P+1):
        if santa_stun[i] > 0:
            santa_stun[i] -= 1

for time in range(M):
    l_move(time)
    # if time == 0:
    #     print(graph)
    #     print(l_l)
    #     print(santa_life)
    #     print(santa_stun)
    s_move(time)
    # if time == 0:
    #     print(graph)
    #     print(l_l)
    if any(santa_life) == False:
        break
    plus_one()
    stun_minus()



print(' '.join(map(str,santa_score[1:])))