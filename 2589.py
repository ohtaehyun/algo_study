import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

map_list = [[] for i in range(N)]
searched = [[-1 for i in range(M)] for j in range(N)]

def search(x,y):
    global N
    global M
    global map_list
    global searched

    result = 0
    q = deque([[x,y,0]])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[-1 for i in range(M)] for j in range(N)]
    visited[x][y] = 0
    while q:
        now_x,now_y,dist = q.popleft()
        if result < dist :
            result = dist

        u,d,r,l = False,False,False,False

        for i in range(4):
            nx,ny = now_x + dx[i] , now_y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if map_list[nx][ny] == 1 and (visited[nx][ny] == -1 or dist+1 < visited[nx][ny]):
                    visited[nx][ny] = dist + 1
                    q.append([nx,ny,dist+1])
    return result


for i in range(N):
    map_str = input().rstrip()
    for c in map_str:
        kind = 0 if c == 'W' else 1
        map_list[i].append(kind)


max_length = -1
ans = -1
for i in range(N):
    for j in range(M):
        if map_list[i][j] == 1:
            searched[i][j] = 1
            result = search(i,j)
            if ans < result :
                ans = result
print(ans)