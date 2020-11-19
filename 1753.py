import sys
from heapq import heappush,heappop
input = sys.stdin.readline

v,e = map(int,input().split())
s = int(input())
s-=1
visited = [False for i in range(v)]
visited[s]=0
edge_list = [ [] for i in range(v) ]

for _ in range(e):
    u,v,w = map(int,input().split())
    edge_list[u-1].append((v-1,w))

heap = []
heappush(heap,[0,s])
while heap:
    now_w,now = heappop(heap)
    for n,w in edge_list[now]:
        if visited[n] is False or now_w + w < visited[n]:
            heappush(heap,[now_w+w,n])
            visited[n] = now_w + w 


for v in visited:
    if v is False :
        print('INF')
    else :
        print(v)