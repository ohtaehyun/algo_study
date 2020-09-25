import sys
from collections import deque
input= sys.stdin.readline

def bfs(map_list,x:int,y:int,height:int,width:int):
    move_x = [ -1, 1, 0, 0 ]
    move_y = [ 0, 0, 1, -1 ]

    queue = deque()
    queue.append((x,y))

    visited =[ [-1 for i in range(width)] for j in range(height)]
    visited[x][y] = 0
    while queue:
        now_x,now_y = queue.popleft()
        now_cnt = visited[now_x][now_y]
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if next_x < 0 or next_x >= height  or next_y < 0 or next_y >= width :
                continue
            if visited[next_x][next_y] != -1 :
                continue
            
            if map_list[next_x][next_y] == '*':
                pass
            elif map_list[next_x][next_y] == '#':
                visited[next_x][next_y] = now_cnt+1
                queue.append((next_x,next_y))
            else :
                visited[next_x][next_y] = now_cnt
                queue.appendleft((next_x,next_y))
    return visited
N = int(input())
for i in range(N):
    map_list = []
    h,w = map(int,input().split())
    w += 2
    map_list.append('.' * w)
    for j in range(h):
        map_list.append('.'+input().rstrip()+'.')
    map_list.append('.'*w)
    h += 2

    sang_guen = bfs(map_list,0,0,h,w)
    prisoner_list = []
    for x in range(h):
        for idx,y in enumerate(map_list[x]):
            if y == '$':
                prisoner_list.append((x,idx))
    prisoner_do = []
    for prisoner in prisoner_list:
        x,y = prisoner
        prisoner_do.append(bfs(map_list,x,y,h,w))
    
    prisoner_one = prisoner_do[0]
    prisoner_two = prisoner_do[1]

    ans = 15000

    for x in range(h):
        for y in range(w):
            if map_list[x][y] != '*':  
                tmp = sang_guen[x][y] + prisoner_one[x][y] + prisoner_two[x][y]
                if map_list[x][y] == '#':
                    tmp -= 2
                
                if tmp < ans:
                    ans = tmp
    print(ans)
