from collections import deque

n, k = map(int, input().split())
graph = deque(list(map(int, input().split())))
people = [0] * n

def move():
    x = graph.pop()
    graph.appendleft(x)

    for i in range(n-2,-1,-1):
        if people[i] == 1:
            people[i],people[i+1] = people[i+1], people[i]

    if people[-1] == 1:
        people[-1] = 0           

def people_move():

    for i in range(n-2,-1,-1):
        if people[i] == 1:
            if people[i+1] == 0 and graph[i+1] != 0:
                people[i],people[i+1] = people[i+1], people[i]
                graph[i+1] -= 1

    if people[-1] == 1:
        people[-1] = 0

def up_people():
    if people[0] == 0 and graph[0] != 0:
        people[0] = 1
        graph[0] -= 1

def check():
    cnt = 0
    for i in graph:
        if i == 0:
            cnt += 1
    
    if cnt >= k:
        return True
    else:
        return False

time = 0
while True:
    time += 1
    move()
    people_move()
    up_people()

    if check():
        break

print(time)