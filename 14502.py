import sys
import copy
from collections import deque
input = sys.stdin.readline
diff_x = [ -1, 1, 0, 0]
diff_y = [ 0, 0, 1, -1]
N,M = map(int,input().split())
map_list = []
virus = []
ans = -1
for i in range(N):
    input_list = [ int(t) for t in input().split()]
    map_list.append(input_list)
    for j in range(M):
        if input_list[j] == 2:
            virus.append((i,j))

def getCount(map_list):
    global virus
    global ans
    global N
    queue = virus.copy() 
    while queue:
        nox_x, now_y = queue.pop(0)

        for i in range(4):
            next_x = nox_x + diff_x[i]
            next_y = now_y + diff_y[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            if map_list[next_x][next_y] != 0 :
                continue
            queue.append((next_x,next_y))
            map_list[next_x][next_y] = 2

    cnt = 0 
    for i in range(N):
        cnt += map_list[i].count(0)

    if ans < cnt :
        ans = cnt 



def build_wall(wall_cnt,start):
    global N
    global M
    global map_list
    if wall_cnt == 3:
        getCount(copy.deepcopy(map_list))
        return 
    for i in range(start,N*M):
        row = i//M
        col = i % M 
        if map_list[row][col] == 0 :
            map_list[row][col] = 1
            build_wall(wall_cnt+1,i+1)
            map_list[row][col] = 0 

build_wall(0,0)
print(ans)
