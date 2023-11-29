n, m = map(int, input().split())

graph = []
total = 0
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,1,1,0,-1,-1,-1,0,1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

yung = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

def over_move(y, direction):
    if y + direction >= n:
        new_direction = direction % (n-1)
    else:
        new_direction = direction
    return new_direction


def yung_move(d,p):
    for i in range(len(yung)):
        yung[i][0] += over_move(yung[i][0], dx[d] * p)
        yung[i][1] += over_move(yung[i][0], dy[d] * p)

def grow():
    for i in yung:
        graph[i[0]][i[1]] += 1

def cross():
    c = [2,4,6,8]
    for i in yung:
        count = 0
        for j in c:
            if 0 <= (i[0] + dx[j]) < n and 0 <= (i[1] + dy[j]) < n:
                if graph[i[0] + dx[j]][i[1] + dy[j]] >= 1:
                    count += 1
        graph[i[0]][i[1]] += count

def search_tree():
    new_yung = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and [i,j] not in yung:
                graph[i][j] -= 2
                new_yung.append([i,j])
    return new_yung

for _ in range(m):
    d,p = map(int, input().split())
    yung_move(d,p)
    grow()
    cross()
    yung = search_tree()

for i in graph:
    for j in i:
        total += j

print(total)