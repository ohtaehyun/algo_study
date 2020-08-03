goal = int(input())

visited = [[False for i in range(2001)] for j in range(2001)]
visited [1][0] = 0 
queue = [(1,0)]

while queue:
    x,y = queue.pop(0)
    if x == goal:
        print(visited[x][y])
        break
    if x>0  and visited[x-1][y] is False:
        visited[x-1][y] = visited[x][y] + 1
        queue.append((x-1,y))
    
    if visited[x+y][y] is False and x+y < 1001 :
        visited[x+y][y] = visited[x][y]+1
        queue.append((x+y,y))

    if visited[x][x] is False :
        visited[x][x] = visited[x][y] + 1
        queue.append((x,x))
