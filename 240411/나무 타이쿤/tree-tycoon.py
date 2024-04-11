n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

drug = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

ddx = [-1,-1,1,1]
ddy = [-1,1,-1,1]

for _ in range(m):
    # 방향, 이동 칸 수
    d,p = map(int, input().split())

    tmp_drug = []
    # 약 이동 후 높이 증가
    for x,y in drug:
        nx, ny = (x + dx[d-1] * p) % n, (y + dy[d-1] * p) % n
        graph[nx][ny] += 1
        tmp_drug.append([nx,ny])

    for x,y in tmp_drug:
        cnt = 0
        for z in range(4):
            nnx,nny = x + ddx[z], y + ddy[z]

            if 0 <= nnx < n and 0 <= nny <n and graph[nnx][nny] >= 1:
                    cnt += 1
        graph[x][y] += cnt

    tmp = []
    # 2이상 식물 잘라내기
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and [i,j] not in tmp_drug:
                graph[i][j] -= 2
                tmp.append([i,j])
    drug = tmp

result = 0
for i in range(n):
    result += sum(graph[i])

print(result)