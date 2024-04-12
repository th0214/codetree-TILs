from collections import deque

N, M, C = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

c_x, c_y = map(int, input().split())
c_l = [c_x-1, c_y-1]

p_l = [[0]]
p_life = [True] * (M+1)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(1, M+1):
    x,y,a,b = map(int, input().split())
    p_l.append([x-1,y-1,a-1,b-1])

def find_person():
    global C, c_l
    tmp = []
    check = True
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((c_l[0],c_l[1]))
    visited[c_l[0]][c_l[1]] = 0
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

    for idx in range(1,len(p_l)):
        if p_life[idx] == True:
            x,y,a,b = p_l[idx]
            if visited[x][y] == -1:
                return False
            tmp.append((visited[x][y], x,y,idx))
    
    tmp.sort(key=lambda x:(x[0],x[1],x[2]))
    c_l = [tmp[0][1],tmp[0][2]]
    C -= tmp[0][0]
    if C <= 0:
        return False
    else:
        return tmp[0][3]


def go_destination(idx):
    global c_l, C

    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((c_l[0],c_l[1]))
    visited[c_l[0]][c_l[1]] = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

    if visited[p_l[idx][2]][p_l[idx][3]] == -1:
        return False
    else:
        if C - (visited[p_l[idx][2]][p_l[idx][3]]-1) >= 0:
            C += (visited[p_l[idx][2]][p_l[idx][3]]-1)
            p_life[idx] = False
            c_l = [p_l[idx][2],p_l[idx][3]]
        else:
            return False
    
    return True



while True:
    result = find_person()
    if result == False:
        print(-1)
        break
    result1 = go_destination(result)

    if result1 == False:
        print(-1)
        break

    if any(p_life[1:]) == False:
        print(C)
        break