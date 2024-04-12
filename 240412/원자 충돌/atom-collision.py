n,m,k = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for idx in range(m):
    x,y,m,s,d = map(int, input().split())

    graph[x-1][y-1].append([m,s,d])

def move():
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]):
                while len(graph[i][j]):
                    m,s,d = graph[i][j].pop()

                    nx, ny = (i + dx[d]*s) % n, (j + dy[d]*s) % n
                    tmp[nx][ny].append([m,s,d])
    
    return tmp

def combine(graph):
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    cross_d = [1,3,5,7]
    updown_d = [0,2,4,6]
    for i in range(n):
        for j in range(n):
            t_s = 0
            t_m = 0
            cross = False
            updown = False
            if len(graph[i][j]) >= 2:
                length = len(graph[i][j])
                while len(graph[i][j]):
                    m,s,d = graph[i][j].pop()
                    if d in cross_d:
                        cross = True
                    elif d in updown_d:
                        updown = True
                    t_m += m
                    t_s += s
            if t_m //5 > 0:
                if cross == True and updown == True:
                    for l in cross_d:
                        tmp[i][j].append([t_m//5,t_s//length,l])

                elif cross == True and updown == False:
                    for l in updown_d:
                        tmp[i][j].append([t_m//5,t_s//length,l])
                
                elif cross == False and updown == True:
                    for l in updown_d:
                        tmp[i][j].append([t_m//5,t_s//length,l])
            elif len(graph[i][j]) == 1:
                tmp[i][j] = graph[i][j]

    return tmp

for _ in range(k):
    graph = move()
    graph = combine(graph)

result = 0
for i in range(n):
    for j in range(n):
        if len(graph[i][j]):
            for k in range(len(graph[i][j])):
                result += graph[i][j][k][0]

print(result)