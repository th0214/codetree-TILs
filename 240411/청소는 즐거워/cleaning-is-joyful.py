n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

left = [(-2,0,0.02),(2,0,0.02),(-1,0,0.07),(1,0,0.07),(1,1,0.01),(-1,1,0.01),(1,-1,0.1),(-1,-1,0.1),(0,-2,0.05),(0,-1,0)]
right = [(x,-y,z) for x,y,z in left] 
down = [(-y,x,z) for x,y,z in left]
up = [(-x,y,z) for x,y,z in down]
arrow = {0:left, 1:down, 2:right, 3:up}
answer = 0
def move(x,y,direction):
    global answer

    tmp = [[0] * n for _ in range(n)]
    out_sand = 0
    total_sand = 0

    for i,j,idx in arrow[direction]:
        nx, ny = i + x, j + y

        if 0 <= nx < n and 0 <= ny < n:
            if idx == 0:
                tmp[nx][ny] = (graph[x][y] - total_sand)
                break
            total_sand += int(graph[x][y] * idx)
            tmp[nx][ny] = int(graph[x][y] * idx)

        elif not (0 <= nx < n and 0 <= ny < n):
            if idx == 0:
                out_sand += (graph[x][y] - total_sand)
                break
            total_sand += int(graph[x][y] * idx)
            out_sand += int(graph[x][y] * idx)

    for i in range(n):
        for j in range(n):
            graph[i][j] += tmp[i][j]
    graph[x][y] = 0
    answer += out_sand

def curve_move():
    global answer

    direction = 0
    num = 1
    x,y = n//2, n//2
    # nx, ny = x + dx[direction], y + dy[direction]
    # move(nx,ny,direction)

    while True:

        for _ in range(1, num+1):
            nx, ny = x + dx[direction], y + dy[direction]

            move(nx,ny,direction)
            if (nx,ny) == (0,0):
                return answer

            x,y = nx, ny

        direction = (direction + 1) % 4

        if direction == 0 or direction == 2:
            num += 1

print(curve_move())