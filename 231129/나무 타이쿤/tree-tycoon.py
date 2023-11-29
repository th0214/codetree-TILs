n, m = map(int, input().split())

graph = []
total = 0
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,1,1,0,-1,-1,-1,0,1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

yung = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

def over_move(direction):
    if direction > n-1:
        direction = direction % (n-1)
    else:
        direction = direction
    return direction


def yung_move(d,p):
    for i in range(len(yung)):
        yung[i][0] += over_move(dx[d] * p)
        yung[i][1] += over_move(dy[d] * p)
    return yung

def grow():
    for i in yung:
        graph[i[0]][i[1]] += 1

def cross():
    c = [[1,1],[-1,-1],[-1,1],[1,-1]]
    for i in yung:
        count = 0
        for j in c:
            if (i[0] + j[0]) < n and (i[1] + j[1]) < n:
                if graph[i[0] + j[0]][i[1] + j[1]] >= 1:
                    count += 1
        graph[i[0]][i[1]] += count

def search_tree():
    global yung
    new_yung = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and [i,j] not in yung:
                graph[i][j] -= 2
                new_yung.append([i,j])
    yung = new_yung

for _ in range(m):
    d,p = map(int, input().split())
    yung_move(d,p)
    grow()
    cross()
    search_tree()

for i in graph:
    for j in i:
        total += j

print(total)