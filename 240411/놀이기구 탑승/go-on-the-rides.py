n = int(input())
di = dict()
graph = [[0] * n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n*n):
    n0, n1, n2, n3, n4 = map(int, input().split())

    di[n0] = [n1, n2, n3, n4]

    tmp = []
    for i in range(n):
        for j in range(n):
            like, blank = 0, 0
            if graph[i][j] == 0:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in [n1, n2, n3, n4]:
                            like += 1
                        if graph[nx][ny] == 0:
                            blank += 1
                tmp.append([like,blank,i,j])
    
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    graph[tmp[0][2]][tmp[0][3]] = n0

cnt = 0
score = [0,1,10,100,1000]
result = 0

for i in range(n):
    for j in range(n):

        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in di[graph[i][j]]:
                    cnt += 1
        
        result += score[cnt]
        cnt = 0

print(result)