from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

group_n = 0
group = [[0] * n for _ in range(n)]
group_cnt = {}
visited = [[False] * n for _ in range(n)]


# (x, y) 위치에서 DFS를 진행합니다.
def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 인접한 칸 중 숫자가 동일하면서 방문한 적이 없는 칸으로만 이동이 가능합니다.
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
            visited[nx][ny] = True
            group[nx][ny] = group_n
            group_cnt[group_n] += 1
            dfs(nx, ny)


# 그룹을 만들어줍니다.
def find_group(t):
    global group_n

    group_n = 0

    # visited 값을 초기화 해줍니다.
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # DFS를 이용하여 그룹 묶는 작업을 진행합니다.
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                visited[i][j] = True
                group[i][j] = group_n
                group_cnt[group_n] = 1
                dfs(i, j)


def calculate():
    result = 0

    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n and group[i][j] != group[nx][ny]:
                    num1, num2 = graph[i][j], graph[nx][ny]
                    all1, all2 = group_cnt[group[i][j]], group_cnt[group[nx][ny]]
                    result += (all1+all2) * num1 * num2
    
    return result // 2


def rotate(n1,n2,z1,z2):
    tmp = [[0] * n for _ in range(n)]

    for i in range(z1,n1):
        for j in range(z2,n2):
            ox, oy = i-z1, j-z2
            fx, fy = oy, (n//2) - ox - 1
            tmp[fx+z1][fy+z2] = graph[i][j]

    # print(tmp)      
    for i in range(z1,n1):
        for j in range(z2,n2):
            graph[i][j] = tmp[i][j]

def cross_rotate():
    tmp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):

            if j == n//2:
                tmp[j][i] = graph[i][j]
            elif i == n//2:
                tmp[n-j-1][i] = graph[i][j]
    
    for i in range(n):
        for j in range(n):
            if j == n//2:
                graph[i][j] = tmp[i][j]
            elif i == n//2:
                graph[i][j] = tmp[i][j]



def total_rotate():
    cross_rotate()
    rotate(half_x,half_y,0,0)
    rotate(half_x,n,0,half_y+1)
    rotate(n,half_y,half_x+1,0)
    rotate(n,n,half_x+1,half_y+1)
    




for t in range(4):

    find_group(t)
    answer += calculate()

    half_x, half_y = n//2, n//2

    total_rotate()

        

print(answer)