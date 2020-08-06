N = int(input())
edge_list = [ [ ] for i in range(N)]


def bfs(start):
    global edge_list
    global result
    visited = [False for i in range(N)] 

    queue = [start]
    
    while queue :
        now = queue.pop()
        for edge in edge_list[now]:
            if visited[edge] is False:
                visited[edge] = True
                result[start][edge] = 1
                queue.append(edge)

for i in range(N):
    edges = [ int(t) for t in input().split()]
    for j in range(N):
        if edges[j] == 1 :
            edge_list[i].append(j)


result = [ [0 for i in range(N)] for j in range(N)]
queue = [0]
for i in range(N):
    bfs(i)

for re in result:
    print(*re)