import copy
from collections import deque
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

array = [[0] * (4) for _ in range(4)]
result = 0

for i in range(4):
    data = list(map(int, input().split()))

    for j in range(4):
        array[i][j] = [data[j*2],data[j*2+1]-1]

def rotate_dir(dir):
    return (dir + 1) % 8

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)

    return None

def fish_move(array, now_x, now_y):

    for index in range(1, 17):

        position = find_fish(array, index)
        if position != None:
            x,y = position[0], position[1]
            dir = array[x][y][1]

            for _ in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]

                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = dir
                        array[nx][ny], array[x][y] = array[x][y], array[nx][ny]
                        break

                dir = rotate_dir(dir)


def shark_move(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]

    for i in range(4):

        now_x += dx[direction]
        now_y += dy[direction]

        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))

    return positions


def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)

    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    fish_move(array, now_x, now_y)

    positions = shark_move(array, now_x, now_y)

    if len(positions) == 0:
        result = max(result, total)
        return

    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)