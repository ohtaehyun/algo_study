from collections import deque

start,goal = map(int,input().split())
visited = [False for _ in range(200001)]
visited[start] = 0

q = deque()
q.append(start)

while q :
    this = q.popleft()
    
    if this == goal:
        print(visited[this])
        break

    if this*2 < 200000 and visited[this*2] is False:
        visited[this*2] = visited[this]
        q.appendleft(this*2)

    if this  > 0 and visited[this-1] is False:
        visited[this-1] = visited[this] + 1
        q.append(this-1)

    if this < 200000 and visited[this+1] is False:
        visited[this+1] = visited[this] + 1
        q.append(this+1) 