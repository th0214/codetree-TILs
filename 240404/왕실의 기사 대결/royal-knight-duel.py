from collections import deque

L, N, Q = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(L)]
life = [0] * (N+1)
origin_life = [0] * (N+1)
knight = dict()
tmp_knight = dict()
visited_k = [0] * (N+1)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

dmg = [0] * (N+1)

def can_move(idx,d):
    global tmp_knight
    q = deque()
    q.append((idx))

    for i in range(1, N+1):
        dmg[i] = 0
        visited_k[i] = 0
        tmp_knight = dict()

    visited_k[idx] = 1

    while q:
        start = q.popleft()
        r,c,h,w = knight[start]

        nr = r + dx[d]
        nc = c + dy[d]
        tmp_knight[start] = [nr,nc,h,w]
        
        if nr < 0 or nc < 0 or nr + h -1 > L or nc + w - 1 > L:
            return False

        for i in range(nr, nr+h):
            for j in range(nc, nc+w):
                if graph[i][j] == 1:
                    dmg[start] += 1
                elif graph[i][j] == 2:
                    return False

        for i in range(1,N+1):
            if visited_k[i] == 1 or k[i] <= 0:
                continue
            if knight[i][0] > nr + h -1 or knight[i][1] > nc + w -1:
                continue
            if nr > knight[i][0] + knight[i][2] -1 or nc > knight[i][1] + knight[i][3] -1:
                continue

            q.append((i))
            visited_k[i] = 1

    dmg[idx] = 0
    return True

def move(i,d):
    if life[i] <= 0:
        return
    
    if can_move(i,d):
        for i in range(1,N+1):
            life[i] -= dmg[i]
            if i in tmp_knight:
                knight[i] = tmp_knight[i]

    
for i in range(1,N+1):
    r,c,h,w,k = map(int, input().split())
    life[i] = k
    origin_life[i] = k
    knight[i] = [r-1,c-1,h,w]

for z in range(Q):
    i,d = map(int, input().split())
    move(i,d)

answer = 0

for i in range(1, N+1):
    if life[i] > 0:
        answer += origin_life[i] - life[i]

print(answer)