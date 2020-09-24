from collections import deque
N,M = map(int,input().split())

visited=[200001 for i in range(200001)]
visited[N] = 0
min_cnt = 200001
queue = deque()

queue.append(N)
total_cnt = 0
while queue:
    now = queue.popleft()
    cnt = visited[now]
    if now == M:
        if cnt == min_cnt:
            total_cnt +=1
        else :
            min_cnt = cnt
            total_cnt = 1
        continue
    if now*2 < 200000 and visited[now*2] >= cnt+1:
        visited[now*2] = cnt+1
        queue.append(now*2)
    if now+1 < 100000 and visited[now+1] >= cnt+1:
        visited[now+1] = cnt+1
        queue.append(now+1)

    if now-1 > -1 and visited[now-1] >= cnt+1:
        visited[now-1] = cnt+1
        queue.append(now-1)

print(visited[M])
print(total_cnt)