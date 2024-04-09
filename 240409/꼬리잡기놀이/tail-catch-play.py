import copy
from collections import deque

N, M, K = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
graph_idx = [[-1] * (N) for _ in range(N)]

v = [[] for _ in range(M)]
tail = [0] * M

visited = [[False] * N for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = 0

def dfs(x,y,idx):
    visited[x][y] = True
    graph_idx[x][y] = idx
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue

        if graph[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue

        if len(v[idx]) == 1 and graph[nx][ny] != 2:
            continue

        v[idx].append((nx,ny))
        if graph[nx][ny] == 3:
            tail[idx] = len(v[idx])
        dfs(nx,ny,idx) 


def init():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                v[cnt].append((i,j))
                cnt += 1
    
    for i in range(M):
        x,y = v[i][0]
        dfs(x,y,i)

def move():
    
    for i in range(M):
        tmp = v[i][-1]
        for j in range(len(v[i]) -1,0,-1):
            v[i][j] = v[i][j-1]
        v[i][0] = tmp
    
    for i in range(M):
        for j, (x,y) in enumerate(v[i]):
            if j == 0:
                graph[x][y] = 1
            elif j < tail[i]-1:
                graph[x][y] = 2
            elif j == tail[i]-1:
                graph[x][y] = 3
            else:
                graph[x][y] = 4
        
def throw(turn):
    turn = (turn) % (4*N)
    
    if turn <= N:
        for i in range(N):
            if 1<= graph[turn-1][i] <= 3:
                get_score(turn-1, i)
                return graph_idx[turn-1][i]
    
    if N+1 <= turn <= 2*N:
        turn -= N
        for i in range(N):
            if 1<= graph[N-1-i][turn-1] <= 3:
                get_score(i,turn-1)
                return graph_idx[i][turn-1]
    
    if (2*N+1) <= turn <= (3*N):
        turn -= 2*N
        for i in range(N):
            if 1 <= graph[N-turn][N-i-1] <= 3:
                get_score(N-turn,N-i-1)
                return graph_idx[N-turn][N-i-1]
    
    if (3*N+1) <= turn <= (4*N):
        turn -= 3*N
        for i in range(N):
            if 1 <= graph[i][N-turn] <= 3:
                get_score(i,N-turn)
                return graph_idx[i][N-turn]

    else:
        return -1

def get_score(x,y):
    global answer

    idx = graph_idx[x][y]
    value = v[idx].index((x,y))
    answer += (value+1) * (value+1)

def reverse(idx):

    if idx == -1:
        return
    
    new_v = []

    for j in range(tail[idx] - 1, -1, -1):
        new_v.append(v[idx][j])

    for j in range(len(v[idx]) - 1, tail[idx] - 1, -1):
        new_v.append(v[idx][j])

    v[idx] = new_v[:]

    # 벡터에 저장한 정보를 바탕으로 보드의 표기 역시 바꿔줍니다.
    for j, (x, y) in enumerate(v[idx]):
        if j == 0:
            graph[x][y] = 1
        elif j < tail[idx] - 1:
            graph[x][y] = 2
        elif j == tail[idx] - 1:
            graph[x][y] = 3
        else:
            graph[x][y] = 4
    

init()
for i in range(1,K+1):
    move()
    # if i == 4:
    #     print(graph)
    #     print(v)
    idx = throw(i)

    reverse(idx)
    # if i == 4:
    #     print(graph)
    #     print(v)

print(answer)