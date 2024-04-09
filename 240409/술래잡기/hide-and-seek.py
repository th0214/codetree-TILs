n,m,h,k = map(int, input().split())

graph = [[0] * n for _ in range(n)]
p_graph = [[[] for _ in range(n)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

s_dx, s_dy = [-1, 0, 1, 0], [0, 1, 0, -1]

s_x = n // 2
s_y = n // 2
s_l = [s_x,s_y]

seeker_next_dir = [[0] * n for _ in range(n)]
seeker_rev_dir = [[0] * n for _ in range(n)]

right = True
result = 0

for _ in range(m):
    x,y,d = map(int, input().split())
    p_graph[x-1][y-1].append(d-1)

for _ in range(h):
    x,y = map(int, input().split())
    graph[x-1][y-1] = 1

def is_avail(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def t_move(k):
    tmp = []
    tmp_graph = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if len(p_graph[i][j]) and is_avail(i,j,s_l[0],s_l[1]) <= 3:
                tmp.append([i,j])

    # if k == 4:
    #     print(k,tmp)

    if len(tmp):
        for x,y in tmp:
            
            while len(p_graph[x][y]):
                d = p_graph[x][y].pop()

                # if k == 4:
                #     print(k,d,x,y)
                    
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < n and 0 <= ny < n:
                    if (nx,ny) != (s_l[0],s_l[1]):
                        tmp_graph[nx][ny].append(d)
                    else:
                        tmp_graph[x][y].append(d)
                else:
                    d = (d+2) % 4
                    nx, ny = x + dx[d], y + dy[d]
                    if (nx,ny) != (s_l[0],s_l[1]):
                        tmp_graph[nx][ny].append(d)
                    else:
                        tmp_graph[x][y].append(d)

        for i in range(n):
            for j in range(n):
                if len(tmp_graph[i][j]):
                    while len(tmp_graph[i][j]):
                        p_graph[i][j].append(tmp_graph[i][j].pop())


def initialize_seeker_path():
    # 상우하좌 순서대로 넣어줍니다.
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 시작 위치와 방향, 
    # 해당 방향으로 이동할 횟수를 설정합니다. 
    curr_x, curr_y = n // 2, n // 2
    move_dir, move_num = 0, 1

    while True:
        # move_num 만큼 이동합니다.
        for _ in range(move_num):
            seeker_next_dir[curr_x][curr_y] = move_dir
            curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]
            seeker_rev_dir[curr_x][curr_y] = move_dir + 2 if move_dir < 2 else move_dir - 2

            # 이동하는 도중 (0, 0)으로 오게 되면,
            # 움직이는 것을 종료합니다.
            if (curr_x, curr_y) == (0,0):
                return
        
        # 방향을 바꿉니다.
        move_dir = (move_dir + 1) % 4
        # 만약 현재 방향이 위 혹은 아래가 된 경우에는
        # 특정 방향으로 움직여야 할 횟수를 1 증가시킵니다.
        if move_dir == 0 or move_dir == 2:
            move_num += 1

def s_move():
    global right, s_l

    x,y = s_l

    if right == True:
        nx, ny = x + s_dx[seeker_next_dir[x][y]], y + s_dy[seeker_next_dir[x][y]]
        s_l = [nx, ny]

        if (nx,ny) == (0,0):
            right = False
        
        return seeker_next_dir[nx][ny]
    
    else:
        nx, ny = x + s_dx[seeker_rev_dir[x][y]], y + s_dy[seeker_rev_dir[x][y]]
        s_l = [nx, ny]

        if (nx,ny) == (n//2,n//2):
            right = True
        
        return seeker_rev_dir[nx][ny]

def seeker(direction, time):
    global result

    x,y = s_l
    
    for i in range(3):
        nx, ny = x + s_dx[direction]* i, y + s_dy[direction] * i
        if 0 <= nx < n and 0 <= ny < n and len(p_graph[nx][ny]) > 0 and graph[nx][ny] != 1:
            # 잡기
            result += (time * len(p_graph[nx][ny]))
            p_graph[nx][ny] = []

initialize_seeker_path()

for t in range(k):
    # if t == 4:
    #     print(p_graph)
    #     print(graph)
    #     print(s_l)
    t_move(t)
    direction = s_move()
    seeker(direction, (t+1))
    # if t == 4:
    #     print(p_graph)
    #     print(s_l)
print(result)