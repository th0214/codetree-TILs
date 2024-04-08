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

def move_select(idx,x,y):

    nx, ny = x + dx[p_abil[idx][2]], y + dy[p_abil[idx][2]]

    if 0 <= nx < n and 0 <= ny < n:
        return nx, ny
    
    else:
        p_abil[idx][2] = (p_abil[idx][2]+2) % 4
        nx, ny = x + dx[p_abil[idx][2]], y + dy[p_abil[idx][2]]
        return nx, ny
    
def move(idx,x,y):

    rx, ry = p_abil[idx][0], p_abil[idx][1]
    p_graph[rx][ry] = -1

    p_graph[x][y] = idx
    p_abil[idx][0], p_abil[idx][1] = x, y

def get_gun(idx,x,y):

    if p_abil[idx][4] == 0:
        p_abil[idx][4] = max(gun_graph[x][y])
        gun_graph[x][y].pop(gun_graph[x][y].index(max(gun_graph[x][y])))

    else:
        max_gun = max(gun_graph[x][y])
        tmp = p_abil[idx][4]

        if max_gun > tmp:
            p_abil[idx][4] = max_gun
            gun_graph[x][y][gun_graph[x][y].index(max(gun_graph[x][y]))] = tmp   
        
def fight(idx,nx,ny):
    compare_num = p_graph[nx][ny]

    sum1 = p_abil[compare_num][3] + p_abil[compare_num][4]
    sum2 = p_abil[idx][3] + p_abil[idx][4]

    if sum1 > sum2:
        return compare_num, idx, abs(sum1-sum2)
    elif sum1 < sum2:
        return idx, compare_num, abs(sum2-sum1)
    else:
        if p_abil[compare_num][3] > p_abil[idx][3]:
            return compare_num, idx, abs(sum1-sum2)
        elif p_abil[compare_num][3] < p_abil[idx][3]:
            return idx, compare_num, abs(sum2-sum1)

def drop_gun(idx,x,y):

    gun_graph[x][y].append(p_abil[idx][4])
    p_abil[idx][4] = 0

def losermove(idx):
    x,y = p_abil[idx][0], p_abil[idx][1]
    nx, ny = x + dx[p_abil[idx][2]], y + dy[p_abil[idx][2]]

    while not (0 <= nx < n and 0 <= ny < n) and p_graph[nx][ny] == -1:
        p_abil[idx][2] = (p_abil[idx][2] + 1) % 4
        nx, ny = x + dx[p_abil[idx][2]], y + dy[p_abil[idx][2]]

    return nx,ny

def simul():

    for i in range(m):
        x,y = p_abil[i][0], p_abil[i][1]

        nx,ny = move_select(i,x,y)
        if p_graph[nx][ny] == -1:
            if len(gun_graph[nx][ny]) == 0:
                move(i, nx,ny)
            else:
                get_gun(i, nx,ny)
                move(i, nx,ny)
        else:
            win_idx, lose_idx, diff_num = fight(i,nx,ny)
            score[win_idx] += diff_num
            move(i,nx,ny)
            # 진 사람
            drop_gun(lose_idx, nx,ny)
            lx, ly = losermove(lose_idx)
            move(lose_idx,lx,ly)
            if len(gun_graph[lx][ly]) != 0:
                get_gun(lose_idx,lx,ly)

            # 이긴 사람
            get_gun(win_idx,nx,ny)
            p_graph[nx][ny] = win_idx
    

for _ in range(k):
    simul()

# print(p_graph)
# print(gun_graph)
# print(p_abil)
# print(score)
print(' '.join(map(str, score)))