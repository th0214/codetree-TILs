n, m, k = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 0:
            continue
        graph[i][j].append(row[j])

person = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    x,y,d,s = map(int, input().split())
    person[x-1][y-1].extend([d,s,i,0])

dx = [-1,0,1,0]
dy = [0,1,0,-1]
score = [0 for _ in range(m)]

def check_dir(i,j,nx,ny):
    nnx, nny = nx+ dx[person[i][j][0]],  ny + dy[person[i][j][0]]

    while len(person[nnx][nny]) != 0:
        if len(person[nnx][nny]) >0:
            person[i][j][0] = (person[i][j][0] + 1) % 4
            nnx, nny = nx + dx[person[i][j][0]], ny + dy[person[i][j][0]]
    
    return nnx, nny

def check_dir2(nx,ny):
    nnx, nny = nx+ dx[person[nx][ny][0]],  ny + dy[person[nx][ny][0]]

    while len(person[nnx][nny]) != 0:
        if len(person[nnx][nny]) >0:
            person[nx][ny][0] = (person[nx][ny][0] + 1) % 4
            nnx, nny = nx + dx[person[nx][ny][0]], ny + dy[person[nx][ny][0]]
    
    return nnx, nny


def check_gun(nx,ny):
    if person[nx][ny][3] == 0:
        person[nx][ny][3] = max(graph[nx][ny])
        graph[nx][ny].pop(graph[nx][ny].index(max(graph[nx][ny])))
                    
    else:
        maxGun = max(graph[nx][ny])
        playerGun = person[nx][ny][3]
        if playerGun >= maxGun:
            return
        person[nx][ny][3] = max(graph[nx][ny])
        graph[nx][ny][graph[nx][ny].index(max(graph[nx][ny]))] = playerGun
 
                    
def rotate_dir(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1

def p_move():
    number = 0
    while number != m:
        moved = False
        for i in range(n):
            if moved:
                    break
            for j in range(n):
                if moved:
                        break
                if len(person[i][j]) > 0:
                    if person[i][j][2] == number:
                        nx, ny = i + dx[person[i][j][0]], j + dy[person[i][j][0]]
                        if 0 <= nx < n and 0 <= ny < n:
                            if len(person[nx][ny]) == 0:
                                person[nx][ny] = person[i][j]
                                person[i][j] = []
                                moved = True
                                check_gun(nx,ny)

                            else:
                                f1 = person[nx][ny][1] + person[nx][ny][3]
                                f2 = person[i][j][1] + person[i][j][3]

                                if f1 > f2:
                                    score[person[nx][ny][2]] += f1-f2

                                    if person[i][j][3] > 0:
                                        graph[nx][ny].append(person[i][j][3])

                                    nnx,nny = check_dir(i,j,nx,ny)
                                    person[nnx][nny] = person[i][j]
                                    person[i][j] = []
                                    moved = True
                                    check_gun(nnx,nny)
                                else:
                                    score[person[i][j][2]] += f2 - f1

                                    if person[nx][ny][3] > 0:
                                        graph[nx][ny].append(person[nx][ny][3])
                                    
                                    nnx,nny = check_dir2(nx,ny)
                                    person[nnx][nny] = person[nx][ny]
                                    person[nx][ny] = person[i][j]
                                    moved = True
                                    check_gun(nnx,nny)
                            
                            
                        else:
                            person[i][j][0] = rotate_dir(person[i][j][0])
                            nx, ny = i + dx[person[i][j][0]], j + dy[person[i][j][0]]
                            if len(person[nx][ny]) == 0:
                                person[nx][ny] = person[i][j]
                                person[i][j] = []
                                moved = True
                                check_gun(nx,ny)

                            else:
                                f1 = person[nx][ny][1] + person[nx][ny][3]
                                f2 = person[i][j][1] + person[i][j][3]

                                if f1 > f2:
                                    score[person[nx][ny][2]] += f1-f2

                                    if person[i][j][3] > 0:
                                        graph[nx][ny].append(person[i][j][3])

                                    nnx,nny = check_dir(i,j,nx,ny)
                                    person[nnx][nny] = person[i][j]
                                    person[i][j] = []
                                    moved = True
                                    check_gun(nnx,nny)
                                else:
                                    score[person[i][j][2]] += f2 - f1

                                    if person[nx][ny][3] > 0:
                                        graph[nx][ny].append(person[nx][ny][3])
                                    
                                    nnx,nny = check_dir2(nx,ny)
                                    person[nnx][nny] = person[nx][ny]
                                    person[nx][ny] = person[i][j]
                                    moved = True
                                    check_gun(nnx,nny)
                            
                            
        number += 1


for _ in range(k):
    p_move()

print(*score)