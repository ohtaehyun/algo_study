import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
map_list = []
for i in range(N):
    input_str = input().strip()
    for j in range(M):
        if input_str[j] == 'R':
            red_x = i
            red_y = j
            input_str.replace('B','.')
        
        if input_str[j] == 'B':
            blue_x = i
            blue_y = j
            input_str.replace('B','.')
    map_list.append(input_str)

red_out = False
blue_out = False
visited = []

diff_x = [ -1, 1, 0, 0 ]
diff_y = [ 0, 0, -1, 1 ]

queue = deque()
queue.append((red_x,red_y,blue_x,blue_y,0))
visited.append((red_x,red_y,blue_x,blue_y))
while queue :
    rx,ry,bx,by,cnt = queue.popleft()
    for i in range(4):
        dx,dy = diff_x[i],diff_y[i]
        next_rx, next_ry, next_bx, next_by = rx, ry, bx, by 

        while True : 
            next_rx += dx 
            next_ry += dy
            if map_list[next_rx][next_ry] == 'O':
                break
            elif map_list[next_rx][next_ry] == '#':
                next_rx -= dx
                next_ry -= dy
                break

        while True : 
            next_bx += dx 
            next_by += dy
            if map_list[next_bx][next_by] == 'O':
                break
            elif map_list[next_bx][next_by] == '#':
                next_bx -= dx
                next_by -= dy
                break

        if map_list[next_bx][next_by] == 'O':
            continue

        if map_list[next_rx][next_ry] == 'O':
            print(cnt+1)
            exit()

        if next_bx == next_rx and next_by == next_ry:
            if abs(rx - next_rx) + abs(ry - next_ry) > abs(bx - next_bx) +  abs(by - next_by):
                next_rx -= dx
                next_ry -= dy
            else :
                next_bx -= dx 
                next_by -= dy
        
        if (next_rx,next_ry,next_bx,next_by) not in visited and cnt < 9:
            queue.append((next_rx,next_ry,next_bx,next_by,cnt+1))
            visited.append((next_rx,next_ry,next_bx,next_by))
print(-1)