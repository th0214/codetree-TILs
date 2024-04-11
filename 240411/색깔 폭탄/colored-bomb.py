from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = 0
def find_bomb():
    global answer

    result = []

    for i in range(n):
        for j in range(n):
            tmp = []
            ex_tmp = []
            visited = [[0] * n for _ in range(n)]
            q = deque()
            if graph[i][j] > 0:
                q.append((i,j))
                visited[i][j] == 1
                color = graph[i][j]
                cnt = 0
                red = 0
                while q:
                    x,y = q.popleft()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                            if graph[nx][ny] == 0:
                                q.append((nx,ny))
                                tmp.append([nx,ny])
                                red += 1
                                cnt += 1
                                visited[nx][ny] = 1
                            elif graph[nx][ny] == color:
                                q.append((nx,ny))
                                tmp.append([nx,ny])
                                ex_tmp.append([nx,ny])
                                cnt += 1
                                visited[nx][ny] = 1

                if cnt >= 2:
                    tmp.sort(key=lambda x:(-x[0],x[1]))
                    ex_tmp.sort(key=lambda x:(-x[0],x[1]))
                    if [cnt,red,ex_tmp[0][0],ex_tmp[0][1],tmp] not in result:
                        
                        result.append([cnt,red,ex_tmp[0][0],ex_tmp[0][1],tmp])

    if len(result):
        result.sort(key=lambda x:(-x[0],x[1],-x[2],x[3]))

        for i,j in result[0][4]:
            graph[i][j] = -2

        answer += (result[0][0] * result[0][0])
    
    else:
        return False

def gravity():

    while True:
        check = 0
        for i in range(n-2,-1,-1):
            for j in range(n):
                if graph[i][j] > 0 and graph[i+1][j] == -2:
                    graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
                    check = 1
        if check == 0:
            break

def rotate():
    tmp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            tmp[n-j-1][i] = graph[i][j]
    
    return tmp


while True:
    check = find_bomb()
    if check == False:
        break
    gravity()
    graph = rotate()
    gravity()

print(answer)