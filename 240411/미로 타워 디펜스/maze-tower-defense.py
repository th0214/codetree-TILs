n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

m_l = [n//2,n//2]
result = 0
def attack(d,p):
    global result

    for i in range(1,p+1):
        nx, ny = m_l[0] + dx[d] * i, m_l[1] + dy[d] * i

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] >= 1:
            result += graph[nx][ny]
            graph[nx][ny] = 0

def list_array():
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    tmp = []
    direction = 0
    num = 1
    x,y = n//2, n//2
    while True:
        for i in range(num):
            nx, ny = x + dx[direction], y + dy[direction]
            
            if graph[nx][ny] >= 1:
                tmp.append(graph[nx][ny])

            if nx == 0 and ny == 0:
                return tmp
            
            x,y = nx, ny
        
        direction = (direction + 1) % 4
        if direction == 0 or direction == 2:
            num += 1

def delete(arr):
    global result
    tmp = []
    standard_num = arr[0]
    cnt = 0
    access = False
    for i in range(len(arr)):

        if standard_num == arr[i]:
            cnt += 1
        
        if standard_num != arr[i]:
            if cnt >= 4:
                result += (arr[i-1] * cnt)
                for j in range(1,cnt+1):
                    arr[i-j] = 0
                standard_num = arr[i]
                cnt = 1
                access = True
            else:
                standard_num = arr[i]
                cnt = 1

    if cnt >= 4:
        result += (arr[i-1] * cnt)
        for j in range(1,cnt+1):
            arr[i-j] = 0
        standard_num = arr[i]
        cnt = 1
        access = True
    else:
        standard_num = arr[i]
        cnt = 1

    for i in arr:
        if i >= 1:
            tmp.append(i)
    return tmp, access

def new_array(arr):
    tmp = []
    s_num = arr[0]
    cnt = 0
    for i in range(len(arr)):

        if s_num == arr[i]:
            cnt += 1
        
        if s_num != arr[i]:
            tmp.append(cnt)
            tmp.append(arr[i-1])
            s_num = arr[i]
            cnt = 1

    tmp.append(cnt)
    tmp.append(arr[-1])
    return tmp

def array_list(arr):
    tmp = [[0] * n for _ in range(n)]

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    direction = 0
    num = 1
    x,y = n//2, n//2
    cnt = 0
    while True:
        for i in range(1,num+1):
            nx, ny = x + dx[direction], y + dy[direction]
            tmp[nx][ny] = arr[cnt]
            cnt += 1

            if cnt == len(arr):
                return tmp
            
            if (nx,ny) == (0,0):
                return tmp
            x,y = nx,ny

        direction = (direction+1) % 4
        if direction == 0 or direction == 2:
            num += 1

for _ in range(m):
    d, p = map(int,input().split())

    attack(d, p)
    array = list_array()

    while True:
        array, access = delete(array)

        if access == False:
            break
    
    array = new_array(array)
    graph = array_list(array)

print(result)