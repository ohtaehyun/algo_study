from collections import deque

m,n = map(int,input().split())
miro_list = []

visited = [[ False  for j in range(m)] for i in range(n)]

for i in range(n):
    input_str = input()
    miro_list.append([int(input_str[t]) for t in range(m)])

visited[0][0] = 0

q = deque()
q.append((0,0))
diff_x = [1,-1,0,0]
diff_y = [0, 0, 1, -1]
while q:
    now_x,now_y = q.popleft()
    if now_x == n-1 and now_y == m-1:
        print(visited[n-1][m-1])
        break

    for i in range(4):
        next_x = now_x+diff_x[i]
        next_y = now_y+diff_y[i]
        if 0 <= next_x and next_x < n and 0<=next_y and next_y < m and visited[next_x][next_y] is False:
            if miro_list[next_x][next_y] == 0:
                visited[next_x][next_y] = visited[now_x][now_y]
                q.appendleft((next_x,next_y))
            else:
                visited[next_x][next_y] = visited[now_x][now_y] + 1
                q.append((next_x,next_y))
