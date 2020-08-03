import sys
input = sys.stdin.readline

def bfs(start):
    global visited
    global edge_list
    queue = [start]
    while queue:
        this = queue.pop(0)
        for edge in edge_list[this]:
            if visited[edge] is False:
                visited[edge] = True
                queue.append(edge)

v,e = map(int,input().split())
edge_list = [[] for i in range (v)]

for i in range(e):
    start,end = map(int,input().split())
    edge_list[start-1].append(end-1)
    edge_list[end-1].append(start -1 )

visited = [False for i in range(v)]

cnt = 0 
for i in range(v):
    if visited[i] is False :
        visited[i] = True
        bfs(i)
        cnt+=1
    
print(cnt)