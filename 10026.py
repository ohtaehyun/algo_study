import sys
from collections import deque
input = sys.stdin.readline 

N = int(input())
picture = []
for i in range(N):
    picture.append(input().strip())

blind_picture = []
for i in range(N):
    blind_picture.append(picture[i].replace('G','R'))


diff_x = [-1,1,0,0]
diff_y = [0,0,-1,1]
queue = deque()
queue.append((0,0))

visited=[[0 for i in range(N)] for j in range(N)]
blind_visited = [[0 for i in range(N)] for j in range(N)]

cnt = 0 
blind_cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 :
            cnt += 1
            visited[i][j] = 1
            queue = deque()
            queue.append((i,j))
            color = picture[i][j]
            while queue:
                now_x,now_y = queue.popleft()
                for idx in range(4):
                    next_x, next_y = now_x + diff_x[idx], now_y + diff_y[idx]
                    if 0 <= next_x < N and 0 <= next_y < N:
                        if visited[next_x][next_y] == 0 and picture[next_x][next_y] == color:
                            visited[next_x][next_y] = 1
                            queue.append((next_x,next_y))
        if blind_visited[i][j] == 0 :
            blind_cnt += 1
            blind_visited[i][j] = 1
            queue = deque()
            queue.append((i,j))
            color = blind_picture[i][j]
            while queue:
                now_x,now_y = queue.popleft()
                for idx in range(4):
                    next_x, next_y = now_x + diff_x[idx], now_y + diff_y[idx]
                    if 0 <= next_x < N and 0 <= next_y < N:
                        if blind_visited[next_x][next_y] == 0 and blind_picture[next_x][next_y] == color:
                            blind_visited[next_x][next_y] = 1
                            queue.append((next_x,next_y))
print(cnt,blind_cnt)