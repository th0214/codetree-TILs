n,m,k = map(int, input().split())

score = [0] * m

gun_graph = [[[] for _ in range(n)] for _ in range(n)]
p_graph = [[-1] * n for _ in range(n)]
p_abil = []

for i in range(n):
    num = list(map(int, input().split()))
    for j in range(n):
        if num[j] == 0:
            continue
        gun_graph[i][j].append(num[j])

for i in range(m):
    x,y,d,s = map(int, input().split())
    p_graph[x-1][y-1] = i
    p_abil.append([x-1,y-1,d,s,0])

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def change_gun(idx, x, y):

    if len(gun_graph[x][y]) and max(gun_graph[x][y]) > p_abil[idx][4] and p_abil[idx][4] > 0:
        tmp = p_abil[idx][4]
        p_abil[idx][4] = max(gun_graph[x][y])
        gun_graph[x][y].remove(max(gun_graph[x][y]))
        gun_graph[x][y].append(tmp)
    
    elif len(gun_graph[x][y]) and max(gun_graph[x][y]) > p_abil[idx][4] and p_abil[idx][4] == 0:
        p_abil[idx][4] = max(gun_graph[x][y])
        gun_graph[x][y].remove(max(gun_graph[x][y]))

def sum1_win(i,c_idx,nx,ny,sum1,sum2,x,y):
    global p_graph, gun_graph, p_abil

    score[c_idx] += (sum1 - sum2)
    # 진 사람 총 버리기
    if p_abil[i][4] > 0:
        gun_graph[nx][ny].append(p_abil[i][4])
        p_abil[i][4] = 0
    
    # 이긴 사람 총 줍기
    change_gun(c_idx,nx,ny)

    # 진사람 다른 곳 이동
    dd = p_abil[i][2]
    xx, yy = nx + dx[dd], ny + dy[dd]

    while True:
        
        if not (0 <= xx < n and 0 <= yy < n) or p_graph[xx][yy] != -1:
            dd = (p_abil[i][2]+1) % 4
            xx, yy = nx + dx[dd], ny + dy[dd]
            
        if p_graph[xx][yy] == -1:
            p_abil[i][2] = dd
            p_abil[i][0], p_abil[i][1] = xx,yy
            p_graph[x][y], p_graph[xx][yy] = p_graph[xx][yy], p_graph[x][y]
            break
        
        
    
    # 진 사람 총줍기
    change_gun(i,xx,yy)

def sum2_win(i,c_idx,nx,ny,sum1,sum2,x,y):
    score[i] += (sum2 - sum1)
    # 진 사람 총 버리기
    if p_abil[c_idx][4] > 0:
        gun_graph[nx][ny].append(p_abil[c_idx][4])
        p_abil[c_idx][4] = 0
    
    # 이긴 사람 총 줍기
    change_gun(i,nx,ny)

    # 진사람 다른 곳 이동
    dd = p_abil[c_idx][2]
    xx, yy = nx + dx[dd], ny + dy[dd]
    p_graph[x][y] = -1

    while True:

        if not (0 <= xx < n and 0 <= yy < n) or p_graph[xx][yy] != -1:
            dd = (p_abil[c_idx][2]+1) % 4
            xx, yy = nx + dx[dd], ny + dy[dd]
        
        if p_graph[xx][yy] == -1:
            p_abil[c_idx][2] = dd
            p_abil[c_idx][0], p_abil[c_idx][1] = xx,yy
            p_graph[nx][ny],p_graph[xx][yy] = p_graph[xx][yy], p_graph[nx][ny]
            p_graph[nx][ny] = i
            p_abil[i][0], p_abil[i][1] = nx, ny
            break
        
        
        
    # 진 사람 총줍기
    change_gun(c_idx,xx,yy)


def move():
    global dd
    for i in range(m):
        x,y = p_abil[i][0], p_abil[i][1]

        nx, ny = x + dx[p_abil[i][2]], y + dy[p_abil[i][2]]

        if 0 <= nx < n and 0 <= ny < n:
            if p_graph[nx][ny] == -1:
                p_graph[x][y], p_graph[nx][ny] = p_graph[nx][ny], p_graph[x][y]
                p_abil[i][0], p_abil[i][1] = nx, ny
                change_gun(i, nx, ny)

            else:
                c_idx = p_graph[nx][ny]

                sum1 = p_abil[c_idx][3] + p_abil[c_idx][4]
                sum2 = p_abil[i][3] + p_abil[i][4]

                if sum1 > sum2:
                    sum1_win(i,c_idx,nx,ny,sum1,sum2,x,y)
                    
                elif sum1 < sum2:
                    sum2_win(i,c_idx,nx,ny,sum1,sum2,x,y)
                
                elif sum1 == sum2:
                    if p_abil[c_idx][3] > p_abil[i][3]:
                        sum1_win(i,c_idx,nx,ny,sum1,sum2,x,y)
                    elif p_abil[c_idx][3] < p_abil[i][3]:
                        sum2_win(i,c_idx,nx,ny,sum1,sum2,x,y)

        else:
            dd = (p_abil[i][2] + 2) % 4
            p_abil[i][2] = dd
            nx, ny = x + dx[dd], y + dy[dd]

            if p_graph[nx][ny] == -1:
                p_graph[x][y], p_graph[nx][ny] = p_graph[nx][ny], p_graph[x][y]
                p_abil[i][0], p_abil[i][1] = nx, ny
                change_gun(i, nx, ny)

            else:
                c_idx = p_graph[nx][ny]

                sum1 = p_abil[c_idx][3] + p_abil[c_idx][4]
                sum2 = p_abil[i][3] + p_abil[i][4]

                if sum1 > sum2:
                    sum1_win(i,c_idx,nx,ny,sum1,sum2,x,y)
                    
                elif sum1 < sum2:
                    sum2_win(i,c_idx,nx,ny,sum1,sum2,x,y)
                
                elif sum1 == sum2:
                    if p_abil[c_idx][3] > p_abil[i][3]:
                        sum1_win(i,c_idx,nx,ny,sum1,sum2,x,y)
                    elif p_abil[c_idx][3] < p_abil[i][3]:
                        sum2_win(i,c_idx,nx,ny,sum1,sum2,x,y)

for _ in range(k):
    move()

# print(p_graph)
# print(gun_graph)
# print(p_abil)
# print(score)
print(' '.join(map(str, score)))