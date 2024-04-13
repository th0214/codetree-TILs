red = [[0] * 6 for _ in range(4)]
yellow = [[0] * 4 for _ in range(6)]

k = int(input())
b_block = 0

def red_insert(t,x,y):

    q = 0
    if t == 1:
        while True:
            if red[x][q] == 1:
                break
            q += 1
            if q==6:
                break

        red[x][q-1] = 1

    if t == 2:
        while True:
            if red[x][q] == 1:
                break
            q += 1
            if q==6:
                break
        
        red[x][q-1] = 1
        red[x][q-2] = 1
    
    if t==3:
        while True:
            if red[x][q] == 1 or red[x+1][q] == 1:
                break
            q += 1
            if q==6:
                break
        
        red[x][q-1] = 1
        red[x+1][q-1] = 1

def check_red():
    global b_block
    delete = False
    delete2 = False
    #1자 체크
    for i in range(2,6):
        check = True
        for j in range(4):
            if red[j][i] == 0:
                check = False
                break
            
        if check:
            b_block += 1
            for k in range(4):
                red[j][k] = 0
            
            for tmp_i in range(i,0,-1):
                for tmp_j in range(4):
                    red[tmp_j][tmp_i] = red[tmp_j][tmp_i-1]
                    red[tmp_j][tmp_i-1] = 0
            
    # 연한 부분
    tmp = []

    for i in range(4):
        for j in range(2):
            if red[i][j] == 1:
                tmp.append([i,j])
    
    if len(tmp):
        if abs(tmp[0][0] - tmp[1][0]) == 1:
            red[0][-1] = red[1][-1] = red[2][-1] = red[3][-1] = 0
            delete = True
        
        if abs(tmp[0][1] - tmp[1][1]) == 1:
            red[0][-1] = red[1][-1] = red[2][-1] = red[3][-1] = 0
            red[0][-2] = red[1][-2] = red[2][-2] = red[3][-2] = 0
            delete2 = True

    return delete, delete2

def push_red():

    for l in red:
        l_e = l.pop()
        l.insert(0,l_e)

def yellow_insert(t,x,y):

    q = 0

    if t == 1:
        while True:

            if yellow[q][y] == 1:
                break
            q += 1
            if q == 6:
                break
        
        yellow[q-1][y] = 1
    
    if t == 2:
        while True:

            if yellow[q][y] == 1 or yellow[q][y+1] == 1:
                break
            q += 1
            if q == 6:
                break
        
        yellow[q-1][y] = 1
        yellow[q-1][y+1] = 1
    
    if t == 3:
        while True:

            if yellow[q][y] == 1:
                break
            q += 1
            if q == 6:
                break
        
        yellow[q-1][y] = 1
        yellow[q-2][y] = 1

def check_yellow():
    global b_block
    delete = False
    delete2 = False
    # 1자 체크
    for i in range(2, 6):
        check = True
        for j in range(4):
            if yellow[i][j] == 0:
                check = False
                break
        if check:
            b_block += 1
            for c in range(4):
                yellow[i][c] = 0
            
            for tmp_i in range(i,0,-1):
                for c in range(4):
                    yellow[tmp_i][c] = yellow[tmp_i-1][c]
                    yellow[tmp_i - 1][c]  = 0
            
    # 연한 부분
    tmp = []
    for i in range(2):
        for j in range(4):
            if yellow[i][j] == 1:
                tmp.append([i,j])

    if len(tmp):
        if abs(tmp[0][0] - tmp[1][0]) == 1:
            yellow[-1][0] = yellow[-1][1] = yellow[-1][2] = yellow[-1][3] = 0
            yellow[-2][0] = yellow[-2][1] = yellow[-2][2] = yellow[-2][3] = 0
            delete2 = True
        
        if abs(tmp[0][1] - tmp[1][1]) == 1:
            yellow[-1][0] = yellow[-1][1] = yellow[-1][2] = yellow[-1][3] = 0
            delete = True

    return delete, delete2

def push_yellow():

    tmp = yellow[-1]
    for i in range(5,0,-1):
        yellow[i] = yellow[i-1]
    yellow[0] = tmp


for _ in range(k):
    t, x, y = map(int, input().split())

    # 빨강
    red_insert(t,x,y)
    r1,r2 = check_red()
    if r1 == True:
        push_red()
    elif r2 == True:
        push_red()
        push_red()
    
    # 노랑
    yellow_insert(t,x,y)
    y1,y2 = check_yellow()
    if y1 == True:
        push_yellow()
    elif y2 == True:
        push_yellow()
        push_yellow()

total = 0

for i in red:
    total += sum(i)

for i in yellow:
    total += sum(i)

print(b_block)
print(total)