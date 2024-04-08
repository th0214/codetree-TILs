from collections import deque

n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
d_graph = [[False] * n for _ in range(n)]
h_graph = [[False] * n for _ in range(n)]

p_l = [[0]]
n_l = [[0]]

basecamp = [False] * (m+1)
arrive = [True] * (m+1)

dx = [-1,0,0,1]
dy = [0,-1,1,0]

for i in range(1,m+1):
    x,y = map(int, input().split())
    p_l.append([x-1,y-1])
    n_l.append([x-1,y-1])

def move_basecamp(t):
    tmp = []
    q = deque()
    q.append((p_l[t][0],p_l[t][1],0))
    visited = [[0] * n for _ in range(n)]
    visited[p_l[t][0]][p_l[t][1]] = 1

    while q:
        x,y, cnt = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and h_graph[nx][ny] == False and d_graph[nx][ny] == False:
                if (cnt, nx ,ny) in tmp:
                    pass
                else:
                    tmp.append((cnt,nx,ny))

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and d_graph[nx][ny] == False and h_graph[nx][ny] == False:
                visited[nx][ny] = 1
                q.append((nx,ny,cnt+1))

    tmp.sort(key=lambda x:(x[0],x[1],x[2]))
    # if t == 4:
    #     print(tmp)
    n_l[time] = [tmp[0][1], tmp[0][2]]
    h_graph[tmp[0][1]][tmp[0][2]] = True
    basecamp[time] = True

def go_conv():
    num = []
    
    for i in range(1, m+1):

        if basecamp[i] == True and d_graph[p_l[i][0]][p_l[i][1]] == False:
            num.append(i)
    
    if len(num):
        for i in num:
            tmp = []
            q = deque()
            q.append((n_l[i][0],n_l[i][1],0,-1))
            visited = [[0] * n for _ in range(n)]
            visited[n_l[i][0]][n_l[i][1]] = 1
            
            while q:
                x,y,cnt,direction = q.popleft()

                if x == p_l[i][0] and y == p_l[i][1]:
                    tmp.append((cnt,n_l[i][0],n_l[i][1],direction))

                for j in range(4):
                    nx, ny = x + dx[j], y + dy[j]

                    if 0 <= nx < n and 0 <= ny < n and d_graph[nx][ny] == False and h_graph[nx][ny] == False and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        if cnt == 0:
                            q.append((nx,ny,cnt+1,j))
                        else:
                            q.append((nx,ny,cnt+1,direction)) 
                        
            tmp.sort(key=lambda x:x[0])
            f_x, f_y = tmp[0][1] + dx[tmp[0][3]], tmp[0][2] + dy[tmp[0][3]]

            n_l[i] = [f_x,f_y]

            if (f_x,f_y) == (p_l[i][0],p_l[i][1]):
                arrive[i] = False
                d_graph[f_x][f_y] = True


time = 0

while True:
    if any(arrive[1:]) == False:
        break

    time += 1

    if any(basecamp) == True:
        go_conv()

    if time <= m:
        move_basecamp(time)

# print(d_graph)
# print(p_l)
# print(n_l)

print(time)

# print(time)