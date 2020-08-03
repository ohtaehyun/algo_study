import sys
input = sys.stdin.readline

def dfs(this,edge_list,visited,visited_order):
    visited[this] = True
    visited_order.append(this)

    for edge in edge_list[this]:
        e = edge[1]
        if visited[e] is False :
            dfs(e,edge_list,visited,visited_order)


    return visited_order

def bfs(start,edge_list,length):
    visited = [False for i in range(length+1)]
    queue = [start]
    visited[start] = True
    visited_order = []
    while queue:
        this = queue.pop(0)
        visited_order.append(this)
        for edge in edge_list[this]:
            e = edge[1]
            if visited[e] is False:
                visited[e] = True
                queue.append(e)
    print(*visited_order)
    return 0 

v,e,start = map(int,input().split())

edge_list = [[] for _ in range(v+1)]

for i in range(e):
    start_v,end_v = map(int,input().split())
    edge_list[start_v].append((start_v,end_v))
    edge_list[end_v].append((end_v,start_v))

for i in range(v+1):
    edge_list[i].sort()

print(*dfs(start,edge_list,[False for i in range(v+1)],[]))
bfs(start,edge_list,v)
