import copy

N, M, K = map(int ,input().split())

graph = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        if l[j] > 0:
            graph[i][j].append(l[j])

k_graph = [[[0,0] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if len(graph[i][j]) > 0 :
            k_graph[i][j][0] = graph[i][j][0]
            k_graph[i][j][1] = K

dx = [-1,1,0,0]
dy = [0,0,-1,1]
life = [True] * (M+1)

all_l = [0] + list(map(int, input().split()))
for i in range(len(all_l)):
    all_l[i] = all_l[i] - 1

dic = dict()

people = 1
cnt = 0
for i in range(M*4):
    cnt += 1

    x1,x2,x3,x4 = map(int ,input().split())

    if i >= 4:
        dic[(people,i%4)] = [x1-1,x2-1,x3-1,x4-1]
    else:
        dic[(people,i)] = [x1-1,x2-1,x3-1,x4-1]
    
    if cnt == 4:
        cnt = 0
        people += 1

def minus_k():
    global k_graph

    for i in range(N):
        for j in range(N):
            if k_graph[i][j][1] > 0:
                k_graph[i][j][1] -= 1
                if k_graph[i][j][1] == 0:
                    k_graph[i][j][0] = 0

def p_move():
    tmp = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            check = []
            if len(graph[i][j]):
                for k in range(4):
                    idx = graph[i][j][0]
                    nx, ny = i + dx[dic[(idx,all_l[idx])][k]], j + dy[dic[(idx,all_l[idx])][k]]

                    if 0 <= nx < N and 0 <= ny < N and k_graph[nx][ny][1] == 0:
                        check.append((nx,ny,idx))
                        break
            
                if len(check):
                    tmp[check[0][0]][check[0][1]].append(idx)
                else:
                    # 이동할 땅 없을시
                    check1 = []
                    for k in range(4):
                        idx = graph[i][j][0]
                        nx, ny = i + dx[dic[(idx,all_l[idx])][k]], j + dy[dic[(idx,all_l[idx])][k]]

                        if 0 <= nx < N and 0 <= ny < N and k_graph[nx][ny][0] == idx:
                            check1.append((nx,ny,idx))
                            break

                    tmp[check1[0][0]][check1[0][1]].append(idx)
    
    return tmp
                        
def combine(arr):
    global k_graph, graph
    tmp = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) >= 2:
                min_val = min(arr[i][j])
                for k in arr[i][j]:
                    if k == min_val:
                        tmp[i][j].append(min_val)
                    else:
                        life[k] = False
            elif len(arr[i][j]) == 1:
                tmp[i][j] = arr[i][j]
    
    for i in range(N):
        for j in range(N):
            if len(tmp[i][j]):
                k_graph[i][j][0] = tmp[i][j][0]
                k_graph[i][j][1] = K
    
    graph = tmp

result = -1

for time in range(1, 1001):
    minus_k()
    graph = p_move()
    combine(graph)

    if any(life[2:]) == False:
        result = time
        break

print(result)