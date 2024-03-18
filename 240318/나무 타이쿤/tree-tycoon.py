dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,1,1,0,-1,-1,-1,0,1]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

move = [list(map(int, input().split())) for _ in range(m)]

solar = [[n-1,0],[n-2,0],[n-1,1],[n-2,1]]
new = []
answer = 0

def check(x,y,graph):
    cnt = 0

    for i in range(2,9,2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > 0:
                cnt += 1
    
    if cnt > 0:
        graph[x][y] += cnt

for d, p in move:
    new = []

    for x, y in solar:
        nx = (x+(dx[d]*p)) % n
        ny = (y+(dy[d]*p)) % n
        
        graph[nx][ny] += 1
        new.append([nx,ny])
    
    for i, j in new:
        check(i,j,graph)

    solar = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if [i,j] not in new and graph[i][j] >= 2:
                graph[i][j] -= 2
                solar.append([i,j])


for i in graph:
    for j in i:
        answer += j

print(answer)