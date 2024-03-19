from collections import deque

def find_block(x,y,block_num):
    q = deque()
    q.append((x,y))

    normals = [[x,y]]
    rainbows = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    rainbows.append([nx,ny])
                elif arr[nx][ny] == block_num and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    normals.append([nx,ny])
    for x,y in rainbows:
        visited[x][y] = 0

    return [len(normals + rainbows), len(rainbows), normals+rainbows]

def remove_block(group):
    global score

    score += group[0] ** 2

    for x, y in group[2]:
        arr[x][y] = -2

def gravity():
    # N-2인 이유 -> N-1은 가장 행이 아래여서 더이상 내려갈 수 없다.
    for i in range(N-2, -1, -1):
        for j in range(N):
            if arr[i][j] != -1:
                pointer = i

                while pointer + 1 < N and arr[pointer+1][j] == -2:
                    arr[pointer+1][j] = arr[pointer][j]
                    arr[pointer][j] = -2
                    pointer += 1

def rotate():
    global arr

    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[N-j-1][i] = arr[i][j]
    arr = tmp

N, M = map(int, input().split())

arr = [deque(map(int,input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

score = 0

while True:
    visited = [[0] * N for _ in range(N)]
    groups = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 1 and visited[i][j] == 0:
                visited[i][j] = 1
                group = find_block(i,j,arr[i][j])

                if group[0] >= 2:
                    groups.append(group)

    groups.sort(reverse=True)

    if not groups:
        break

    remove_block(groups[0])
    gravity()
    rotate()
    gravity()

print(score)