import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
map_list = []
size = 2
shark_x = -1
shark_y = -1
MAX_SIZE = 7
for i in range(N):
    input_list = [int(t) for t in input().split()]
    map_list.append(input_list)
    for idx, j in enumerate(input_list):
        if j == 9 :
            shark_x = i
            shark_y = idx 
            map_list[shark_x][shark_y] = 0

def find_fish(shark_x,shark_y,size):
    global N 
    diff_x = [-1,1,0,0]
    diff_y = [0,0,-1,1]
    cnt = N*N + 1
    result = False

    visited_list = [ [False]*N for i in range(N)]
    visited_list[shark_x][shark_y] = True

    eatable_fish = []

    queue = deque()
    queue.append((shark_x,shark_y,0))
    while queue:
        now_x, now_y,now_cnt = queue.popleft() 
        for i in range(4):
            next_x, next_y = now_x + diff_x[i], now_y + diff_y[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N :
                continue
            if visited_list[next_x][next_y] is True :
                continue
            if map_list[next_x][next_y] > size:
                continue
            if map_list[next_x][next_y] == 0 or map_list[next_x][next_y] == size:
                visited_list[next_x][next_y] = True
                queue.append((next_x,next_y,now_cnt+1))
            else :
                visited_list[next_x][next_y] = True
                queue.append((next_x,next_y,now_cnt+1))
                eatable_fish.append((next_x,next_y,now_cnt+1))
    
    if eatable_fish:
        eatable_fish.sort(key = lambda x: (x[2],x[0],x[1]))
        result = (eatable_fish[0][0],eatable_fish[0][1])
        cnt = eatable_fish[0][2]

    return result,cnt
time = 0
eat = 0
while True:
    isFish,cnt = find_fish(shark_x,shark_y,size)
    if isFish is False:
        break
    shark_x,shark_y = isFish
    map_list[shark_x][shark_y] = 0 
    time += cnt
    eat += 1
    if eat == size :
        size += 1
        eat = 0 
print(time)