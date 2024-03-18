n = int(input())

graph = [[0] * n for _ in range(n)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

student = [list(map(int, input().split())) for _ in range(n*n)]
answer = 0
for t in range(n*n):
    n0, n1,n2,n3,n4 = student[t]
    check = []

    for i in range(n):
        for j in range(n):
            
            if graph[i][j] == 0:
                pre, blank = 0, 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in [n1,n2,n3,n4]:
                            pre += 1
                        
                        if graph[nx][ny] == 0:
                            blank += 1
                check.append([i,j,pre,blank])
    
    check.sort(key=lambda x: (-x[2],-x[3],x[i],x[j]))
    graph[check[0][0]][check[0][1]] = n0


score = [0,1,10,100,1000]
for i in range(len(graph)):
    for j in range(len(graph[0])):
        cnt = 0
        for std in student:
            if graph[i][j] == std[0]:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in std[1:]:
                            cnt += 1
                                     
                            
        answer += score[cnt]
print(answer)