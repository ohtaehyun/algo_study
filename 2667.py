import sys
input =sys.stdin.readline


def bfs(x,y):
    global visited
    global arr 
    n = len(arr)
    queue = [(x,y)]
    visited[x][y] = True
    cnt = 1
    while queue :
        this_x,this_y = queue.pop()

        if this_x-1 >= 0 and arr[this_x-1][this_y] != 0 and visited[this_x-1][this_y] is False:
            cnt += 1
            visited[this_x-1][this_y] = True
            queue.append((this_x-1,this_y))

        if this_x+1 < n and arr[this_x+1][this_y] != 0  and visited[this_x+1][this_y] is False:
            cnt += 1
            visited[this_x+1][this_y] = True
            queue.append((this_x+1,this_y))

        if this_y -1  >=  0 and arr[this_x][this_y-1] != 0 and visited[this_x][this_y-1] is False:
            cnt += 1
            visited[this_x][this_y-1] = True
            queue.append((this_x,this_y-1))

        if this_y +1 < n and arr[this_x][this_y+1] != 0  and visited[this_x][this_y+1] is False:
            cnt += 1
            visited[this_x][this_y+1] = True
            queue.append((this_x,this_y+1))

    return cnt

n = int(input())
arr = [] 
visited = [[ False for _ in range(n)] for __ in range(n)]
cnt_list = []

for i in range(n):
    input_str = input()
    arr.append([ int(input_str[i]) for i in range(n)])

for i in range(n):
    for j in range(n):
        if visited[i][j] is False and arr[i][j] == 1:
            result = bfs(i,j)
            if result > 0 :
                cnt_list.append(result)

cnt_list.sort()
print(len(cnt_list))
for cnt in cnt_list:
    print(cnt)