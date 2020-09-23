from collections import deque
T = int(input())

def bfs(start,goal):
    visited = [False for i in range(10000)]
    visited[start] = True
    # cnt_list[start] = 0
    queue = deque()
    queue.append([start,''])
    while queue:
        now,now_cmd= queue.popleft()
        # now_cnt = cnt_list[now]
        if now == goal:
            return now_cmd

        # D연산
        D_result = (2*now) % 10000
        if visited[D_result] is False:
            visited[D_result] = True
            queue.append([D_result,now_cmd +'D'])

        # S연산 
        S_result = 9999 if now == 0 else now-1
        if visited[S_result] is False:
            visited[S_result] = True
            queue.append([S_result,now_cmd +'S'])

        # L연산
        share,remainder = divmod(now,1000)
        L_result = remainder*10 +share
        if visited[L_result] is False:
            visited[L_result] = True
            queue.append([L_result,now_cmd +'L'])

        # R연산
        share,remainder = divmod(now,10)
        R_result = share + remainder*1000
        if visited[R_result] is False:
            visited[R_result] = True
            queue.append([R_result,now_cmd +'R'])

for i in range(T):
    start,goal = map(int,input().split())
    print(bfs(start,goal))
