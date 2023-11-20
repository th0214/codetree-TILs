from collections import deque

n, m = map(int, input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
dice = [1,2,3,4,5,6]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x,y,dir,ans = 0,0,0,0

def move(x,y,dir):
    global dice

    # 동쪽
    if dir == 0:
        dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    # 남쪽
    elif dir == 1:
        dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    # 서쪽
    elif dir == 2:
        dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    # 북쪽
    else:
        dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    
    if dice[5] > maps[x][y]:
        dir = (dir+1) % 4
    elif dice[5] < maps[x][y]:
        dir = (dir+3) % 4

    return dir


def bfs(x,y,an):
    q = deque()
    q.append((x,y))
    visited = [[0]*n for _ in range(n)]
    sum_an = 1
    visited[x][y] = 1

    while q:
        a,b = q.popleft()

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and maps[nx][ny] == an:
                visited[nx][ny] = 1
                q.append((nx,ny))
                sum_an += 1

    return sum_an * an

for _ in range(m):
    nx, ny = x + dx[dir], y + dy[dir]
    if not 0 <= nx < n or not 0 <= ny < n:
        nx, ny = x + dx[dir] * (-1), y + dy[dir] * (-1)
        dir = (dir+2) % 4

    dir = move(nx,ny,dir)
    ans += bfs(nx,ny,maps[nx][ny])
    x,y = nx,ny

print(ans)