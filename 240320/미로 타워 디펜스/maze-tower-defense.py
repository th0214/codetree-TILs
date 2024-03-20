from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

total = [list(map(int, input().split())) for _ in range(m)]
result = 0

def remove(graph, d, p):
    global result
    x = n//2
    y = n//2
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for i in range(1,p+1):
        nx = x + (dx[d]*i)
        ny = y + (dy[d]*i)
        if 0 <= nx < n and 0 <= ny < n:
            result += graph[nx][ny]
            graph[nx][ny] = 0       

def change(graph):
    tmp = []
    nx = n//2
    ny = n//2

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    s = 1
    direction = 0
    over_range = False

    while not over_range:
        for _ in range(2):
            for i in range(s):
                nx += dx[direction]
                ny += dy[direction]

                if not (0 <= nx < n and 0 <= ny < n):
                    over_range = True
                    break

                tmp.append(graph[nx][ny])

            direction = (direction+1) % 4

            # if over_range:
            #     break
        s += 1
    return tmp

def change2(graph):
    tmp = [[0] * n for _ in range(n)]
    nx = n//2 # 3
    ny = n//2 # 3

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    s = 1
    direction = 0
    over_range = False
    cur_num = 0

    while not over_range:
        for _ in range(2):
            for _ in range(s):
                nx += dx[direction]
                ny += dy[direction]

                if not (0 <= nx < n and 0 <= ny < n):
                    over_range = True
                    break
                
                if cur_num < len(graph):
                    if graph[cur_num] != 0:
                        tmp[nx][ny] = graph[cur_num]
                        cur_num += 1
                    else:
                        cur_num += 1
                        tmp[nx][ny] = graph[cur_num]
                    
            direction = (direction + 1) % 4
        s += 1

    return tmp

def move(graph):
    tmp = []
    for i in range(len(graph)):
        if graph[i] != 0:
            tmp.append(graph[i])
    return tmp

def explode(graph):
    global result

    num = graph[0]
    num_count = 0
    state = False

    for i in range(len(graph)):

        if graph[i] == num:
            num_count += 1

        else:
            if num_count >= 4:
                result += (graph[i-1] * num_count)

                for j in range(1,num_count+1):
                    graph[i-j] = 0
                num_count = 1
                state = True
        
            else:
                num = graph[i]
                num_count = 1

    if num_count >= 4:
            result += (graph[i] * num_count)

            for j in range(1,num_count+1):
                graph[i-j+1] = 0
                

    return state, graph 

def make_range(graph):
    tmp = []
    standard = graph[0]
    cnt = 0

    for i in range(len(graph)):
        if graph[i] == standard:
            cnt += 1
        else:
            if cnt > 0:
                tmp.append(cnt)
                tmp.append(graph[i-1])
                standard = graph[i]
                cnt = 1
    
    if cnt > 0:
            tmp.append(cnt)
            tmp.append(graph[i])

    return tmp

for d,p in total:

    remove(graph, d, p)
    graph = change(graph)
    graph = move(graph)

    while True:
        state, graph = explode(graph)
        graph = move(graph)
    
        if not state:
            break 
    graph = make_range(graph)
    graph = change2(graph)

print(result)