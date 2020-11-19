import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N = int(input())
M = int(input())
edge_list = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
for _ in range(M):
    s,e,w = map(int,input().split())
    edge_list[s].append([e,w])

start,end = map(int,input().split())

heap = [] 

heappush(heap,[0,start])
while heap:
    weight,now = heappop(heap)

    for n,n_w in edge_list[now]:
        if visited[n] is False or weight + n_w < visited[n]:
            heappush(heap,[weight+n_w,n])
            visited[n] = weight+n_w


print(visited[end])