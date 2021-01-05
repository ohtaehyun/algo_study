import sys
from collections import deque
input =sys.stdin.readline

N,M = map(int,input().split())

ice = []




def search():
    global N
    global M
    global ice
    visited =[[-1 for i in range(M)] for j in range(N)]
    cnt = 0 #덩어리 숫자
    for i in range(1,N-1):
        for j in range(1,M-1):
            if ice[i][j] != 0 and visited[i][j] == -1 :
                if cnt == 1 :
                    return False
                cnt += 1
                visited[i][j] = 0
                bfs(i,j,visited)
    if cnt == 1 :
        return True
    return False 

def bfs(x,y,visited):
    global N
    global M
    global ice
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque([[x,y]])
    melt_list = [] 
    while q : # 덩어리에 연결된 얼음 검사
        now_x,now_y = q.popleft()

        melt_cnt = 0 
        for i in range(4):
            n_x,n_y = now_x + dx[i] , now_y + dy[i]
            if 0 <= n_x < N and 0 <= n_y < M :
                if ice[n_x][n_y] > 0  and visited[n_x][n_y] == -1 :
                    visited[n_x][n_y] = 0 
                    q.append([n_x,n_y])
                elif ice[n_x][n_y] == 0 :
                    melt_cnt += 1
        if melt_cnt > 0 :
            melt_list.append([now_x,now_y,melt_cnt])
    
    while melt_list : # 얼음이 녹는 부분
        mx,my,mcnt = melt_list.pop()
        ice[mx][my] = 0 if ice[mx][my] <=  mcnt else  ice[mx][my] - mcnt

for _ in range(N):
    ice.append(list(map(int,input().split())))

cnt = 0
while search():
    cnt+=1
if ice == [[0 for i in range(M)] for j in range(N)]:
    print(0)
else :
    print(cnt)

    