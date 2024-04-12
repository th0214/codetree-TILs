from collections import deque

N, M, gas = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
t_x,t_y = map(int, input().split())
tt_x,tt_y = t_x-1,t_y-1
people = [list(map(int, input().split())) for _ in range(M)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check_distance(x,y):
    q = deque()
    q.append((x, y))
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[x][y] = 0

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

    return visited

def check_people(visit):
    tmp = []
    for i in range(len(people)):
        p_x, p_y, d_x, d_y = people[i]
        if visit[p_x-1][p_y-1] >= 0:
            tmp.append([visit[p_x-1][p_y-1],p_x-1,p_y-1,d_x-1,d_y-1,i])
        else:
            return -1

    tmp.sort(key=lambda x: (x[0],x[1],x[2]))

    people.remove(people[tmp[0][5]])

    return tmp

def go(pep):
    global gas
    check = False
    cost, p_x, p_y, d_x, d_y, _ = pep[0]
    gas -= cost

    if gas < 0:
        check = True
        return check, d_x, d_y
    else:
        result = check_destination(p_x,p_y,d_x,d_y)

        gas -= result

        if gas < 0:
            check = True
            return check, d_x, d_y
        else:
            gas += result *2

    return check, d_x,d_y


def check_destination(p_x,p_y,d_x,d_y):
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((p_x,p_y))
    visited[p_x][p_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

    return visited[d_x][d_y]

while people:

    visit = check_distance(tt_x,tt_y)
    pep = check_people(visit)
    if pep == -1:
        gas = -1
        break

    check,tt_x,tt_y = go(pep)

    if check == True:
        gas = -1
        break


print(gas)