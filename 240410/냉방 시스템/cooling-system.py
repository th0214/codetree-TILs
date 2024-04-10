from collections import deque
import copy
n,m,k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
airconditioner = []
office = []
wall = {}

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        else:
            if graph[i][j] == 1:
                office.append((i,j))
            elif graph[i][j] == 2:
                airconditioner.append((i,j,1))
            elif graph[i][j] == 3:
                airconditioner.append((i,j,0))
            elif graph[i][j] == 4:
                airconditioner.append((i,j,3))
            elif graph[i][j] == 5:
                airconditioner.append((i,j,2))
            graph[i][j] = 0

for _ in range(m):
    a,b,c = map(int, input().split())

    if c == 0:
        if (a-1,b-1) in wall:
            wall[(a-1,b-1)].append(0)
        else:
            wall[(a-1,b-1)] = [0]
        if (a-2,b-1) in wall:
            wall[(a-2,b-1)].append(2)
        else:
            wall[(a-2,b-1)] = [2]
    
    elif c == 1:
        if (a-1,b-1) in wall:
            wall[(a-1,b-1)].append(1)
        else:
            wall[(a-1,b-1)] = [1]

        if (a-1,b-2) in wall:
            wall[(a-1,b-2)].append(3)
        else:
            wall[(a-1,b-2)] = [3]

def wind(x,y,d):
    s_x,s_y = x + dx[d], y + dy[d]
    graph[s_x][s_y] += 5
    q = deque()
    q.append((s_x,s_y,4))
    llist = []

    while q:
        x,y,t = q.popleft()
        if t == 0:
            continue
        
        #왼쪽위
        nd = (d + 1) % 4
        nx,ny = x + dx[nd], y + dy[nd]

        if 0 <= nx < n and 0 <= ny < n:
            if (x,y) not in wall or nd not in wall[(x,y)]:
                wx,wy = nx + dx[d], ny + dy[d]
                if (wx,wy) not in llist and 0 <= wx < n and 0 <= wy < n:
                    if (nx,ny) not in wall or d not in wall[(nx,ny)]:
                        llist.append((wx,wy))
                        graph[wx][wy] += t
                        q.append((wx,wy,t-1))
        
        # 직진
        nx, ny = x+dx[d], y+dy[d]
        if 0<=nx<n and 0<=ny<n and (nx,ny) not in llist:
            if (x,y) not in wall or d not in wall[(x,y)]:
                llist.append((nx,ny))
                graph[nx][ny] += t
                q.append((nx,ny,t-1))

        #오른쪽위
        nd = (d-1)%4
        nx, ny = x+dx[nd], y+dy[nd]
        if 0<=nx<n and 0<=ny<n:
            if (x,y) not in wall or nd not in wall[(x,y)]:
                wx, wy = nx+dx[d], ny+dy[d]
                if 0<=wx<n and 0<=wy<n and (nx,ny) not in llist:
                    if (nx,ny) not in wall or d not in wall[(nx,ny)]:
                        llist.append((wx,wy))
                        graph[wx][wy] += t
                        q.append((wx,wy,t-1))

def diffusion():
    tmp_graph = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            
            for k in range(4):
                if (i,j) not in wall or k not in wall[(i,j)]:
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[i][j] >= graph[nx][ny]:
                            tmp_graph[i][j] -= abs(graph[i][j] - graph[nx][ny]) //4
                        elif graph[i][j] < graph[nx][ny]:
                            tmp_graph[i][j] += abs(graph[i][j] - graph[nx][ny]) //4
    
    for i in range(n):
        for j in range(n):
            graph[i][j] += tmp_graph[i][j]

def check():
    
    for a,b in office:
        if graph[a][b] < k:
            return False

    return True
    
for time in range(1,102):

    for x,y,d in airconditioner:
        wind(x,y,d)

    diffusion()

    for i in range(n-1):
        if graph[0][i] > 0:
            graph[0][i] -= 1

        if graph[i][n-1] > 0:
            graph[i][n-1] -=1
        
        if graph[n-1][i+1] > 0:
            graph[n-1][i+1] -= 1
        
        if graph[i+1][0] > 0:
            graph[i+1][0] -=1
    
    if check():
        print(time)
        break

    if time == 101:
        print(-1)