n,m = map(int,input().split())
miro_list = []

visited = [[ [-1,-1]  for j in range(m)] for i in range(n)]
for i in range(n):
    input_str = input()
    miro_list.append([int(input_str[t]) for t in range(m)])

visited[0][0][0] = 1

queue = [(0,0,0)]

while queue:
    x,y,cnt = queue.pop(0)

    for next_x,next_y in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=next_x and next_x <n and 0<=next_y and next_y <m and visited[next_x][next_y][cnt] == -1 :
            if miro_list[next_x][next_y] == 0 :
                visited[next_x][next_y][cnt] = visited[x][y][cnt] + 1
                queue.append((next_x,next_y,cnt))
            elif cnt == 0 :
                visited[next_x][next_y][cnt+1] = visited[x][y][cnt] + 1
                queue.append((next_x,next_y,cnt+1))

result = [ t for t in visited[n-1][m-1] if t > -1]
if len(result) == 0 :
    print(-1)
else :
    print(min(result))