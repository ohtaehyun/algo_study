from collections import deque

def bfs(land,height,sx,sy,length,visited,group):
    q = deque([[sx,sy]])
    visited[sx][sy] = group
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<= nx < length and 0<= ny < length:
                if visited[nx][ny] == -1 and abs(land[x][y] - land[nx][ny]) <= height:
                    visited[nx][ny] = group
                    q.append([nx,ny])
                    
def find_ladder(length,visited,land):
    ladders = set()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(length):
        for j in range(length):
            for k in range(4):
                nx,ny = i+dx[k], j+dy[k]
                if 0<= nx < length and 0<= ny < length:
                    if visited[i][j] != visited[nx][ny]:
                        ladders.add((abs(land[i][j] - land[nx][ny]),visited[i][j],visited[nx][ny]))
    return ladders

def find_root(idx,unions):
    if unions[idx] == idx :
        return idx 
    else:
        unions[idx] = find_root(unions[idx],unions)
        return unions[idx]

def union_check(f,t,unions):
    if find_root(f,unions) == find_root(t,unions):
        return True
    return False

def union(f,t,union):
    r1 = find_root(f,union)
    r2 = find_root(t,union)
    if r1<r2 :
        union[r2] = r1
    else :
        union[r1] = r2
def kruskal(ladders,group):
    if group == 1:
        return 0
    
    ladders = list(ladders)
    ladders.sort()
    
    ans = 0

    unions = [i for i in range(group)]

    for ladder in ladders :
        c,f,t = ladder
        if union_check(f,t,unions) is False:
            union(f,t,unions)
            ans+=c
    return ans

def solution(land, height):
    length = len(land)
    visited = [[-1] * length for i in range(length)]
    group = 1
    for i in range(length):
        for j in range(length):
            if visited[i][j] == -1 :
                bfs(land,height,i,j,length,visited,group)
                group+=1
    ladders = find_ladder(length,visited,land)
    return kruskal(ladders,group)
print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]	,3))