n, m, h, k = map(int, input().split())

hider = [[[] for _ in range(n)] for _ in range(n)]
next_hider = [[[] for _ in range(n)] for _ in range(n)]
tree = [[0] * n for _ in range(n)]
seeker_dir = (n//2,n//2)

seeker_next_dir = [[0] * n for _ in range(n)]
seeker_rev_dir = [[0] * n for _ in range(n)]
ans = 0
forward_facing = True

for _ in range(m):
    x,y,d = map(int, input().split())
    hider[x-1][y-1].append(d)

for _ in range(h):
    x,y = map(int, input().split())
    tree[x-1][y-1] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def initial_seeker_next_path():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    cur_x, cur_y = n // 2, n // 2
    move_dir, move_num = 0, 1

    while cur_x or cur_y:
        for _ in range(move_num):
            seeker_next_dir[cur_x][cur_y] = move_dir
            cur_x, cur_y = cur_x + dx[move_dir], cur_y + dy[move_dir]
            seeker_rev_dir[cur_x][cur_y] = move_dir + 2 if move_dir < 2 else move_dir -2

            if not cur_x and not cur_y:
                break
        
        move_dir = (move_dir + 1) % 4

        if move_dir  == 0 or move_dir == 2:
            move_num += 1
    
def t_move(x,y,direction):
    dtx = [0,0,1,-1]
    dty = [-1,1,0,0]

    nx, ny = x + dtx[direction], y + dty[direction]

    if not in_range(nx, ny):
        direction = 1 - direction if direction < 2 else 5 - direction
        nx, ny = x + dtx[direction], y + dty[direction]
        

    if (nx,ny) != seeker_dir:
        next_hider[nx][ny].append(direction)
    else:
        next_hider[x][y].append(direction)

def t_all_move():

    for i in range(n):
        for j in range(n):
            next_hider[i][j] = []
    
    for i in range(n):
        for j in range(n):
            if len(hider[i][j]) > 0:
                if abs(i-seeker_dir[0]) + abs(j-seeker_dir[1]) <= 3:
                    for direction in hider[i][j]:
                        t_move(i,j,direction)
                else:
                    for move_dir in hider[i][j]:
                        next_hider[i][j].append(hider[i][j])

    for i in range(n):
        for j in range(n):
            hider[i][j] = next_hider[i][j]

def get_seeker_dir():
    x,y = seeker_dir

    move_dir = 0
    if forward_facing:
        move_dir = seeker_next_dir[x][y] 
    else:
        move_dir = seeker_rev_dir[x][y]
    
    return move_dir

def check_facing():
    global forward_facing
    
    if seeker_dir == (0, 0) and forward_facing:
        forward_facing = False

    if seeker_dir == (n // 2, n // 2) and not forward_facing:
        forward_facing = True

def s_move():
    global seeker_dir

    x,y = seeker_dir

    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    move_dir = get_seeker_dir()

    seeker_dir = (x + dxs[move_dir], y + dys[move_dir])

    check_facing()

def get_score(m):
    global ans

    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    x, y = seeker_dir
    move_dir = get_seeker_dir()

    for dist in range(3):
        nx, ny = x + dist * dxs[move_dir], y + dist * dys[move_dir]

        if in_range(nx, ny) and tree[nx][ny] == 0:
            ans += m * len(hider[nx][ny])

            hider[nx][ny] = []


initial_seeker_next_path()

for m in range(1,k+1):
    
    t_all_move()

    s_move()
  
    get_score(m)

print(ans)