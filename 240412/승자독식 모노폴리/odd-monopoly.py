import copy

n, m, K = map(int ,input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
k_graph = [[[0,0] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] > 0 :
            k_graph[i][j][0] = graph[i][j]
            k_graph[i][j][1] = K

dx = [-1,1,0,0]
dy = [0,0,-1,1]
life = [True] * (m+1)

all_l = [0] + list(map(int, input().split()))
for i in range(len(all_l)):
    all_l[i] = all_l[i] - 1

dic = dict()

people = 1
cnt = 0
for i in range(m*4):
    cnt += 1

    x1,x2,x3,x4 = map(int ,input().split())

    if i >= 4:
        dic[(people,i%4)] = [x1-1,x2-1,x3-1,x4-1]
    else:
        dic[(people,i)] = [x1-1,x2-1,x3-1,x4-1]
    
    
    if cnt == 4:
        cnt = 0
        people += 1

def remove_time(tmp_k_graph):
    for i in range(n):
        for j in range(n):
            if tmp_k_graph[i][j][1] > 0:
                tmp_k_graph[i][j][1] -= 1
                if tmp_k_graph[i][j][1] == 0:
                    tmp_k_graph[i][j][0] = 0

    return tmp_k_graph

def fight(tmp):
    tmp1 = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if len(tmp[i][j]) >= 2:
                min_val = min(tmp[i][j])
                for k in tmp[i][j]:
                    if k != min_val:
                        life[k] = False
                tmp1[i][j] = min_val
            if len(tmp[i][j]) == 1:
                tmp1[i][j] = tmp[i][j][0]
    
    return tmp1


def move(graph,k_graph):
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    tmp_k_graph = copy.deepcopy(k_graph)

    tmp_k_graph = remove_time(tmp_k_graph)
 
    for i in range(n):
        for j in range(n):
            check = []
            if graph[i][j] > 0:
                for k in range(4):
                    nx, ny = i + dx[dic[graph[i][j],all_l[graph[i][j]]][k]], j + dy[dic[graph[i][j],all_l[graph[i][j]]][k]]

                    if 0 <= nx < n and 0 <= ny < n and k_graph[nx][ny][1] == 0:
                        check.append([nx,ny,dic[graph[i][j],all_l[graph[i][j]]][k]])
                        break

                if len(check):
                    tmp_k_graph[check[0][0]][check[0][1]][0] = graph[i][j]
                    tmp_k_graph[check[0][0]][check[0][1]][1] = K
                    all_l[graph[i][j]] = check[0][2]
                    tmp[check[0][0]][check[0][1]].append(graph[i][j])
                
                else:
                    for k in range(4):
                        nx, ny = i + dx[dic[graph[i][j],all_l[graph[i][j]]][k]], j + dy[dic[graph[i][j],all_l[graph[i][j]]][k]]

                        if 0 <= nx < n and 0 <= ny < n and k_graph[nx][ny][0] == graph[i][j]:
                            tmp[nx][ny].append(graph[i][j])
                            all_l[graph[i][j]] = dic[graph[i][j],all_l[graph[i][j]]][k]
                            break
    
    tmp = fight(tmp)
    return tmp, tmp_k_graph

def total():
    global graph, k_graph
    for time in range(1,1001):
        graph, k_graph = move(graph,k_graph)

        if life[1] == True and any(life[2:]) == False:
            return time
            
    return -1

print(total())