import sys
input = sys.stdin.readline

n,m = map(int,input().split())

def bfs():
    global visited
    global road_list
    diff_x = [1,-1,0,0]
    diff_y = [0,0,1,-1]
    queue = [(0,0)]
    while queue:
        this_x,this_y = queue.pop(0)

        for i in range(4):
            next_x = this_x + diff_x[i]
            next_y = this_y + diff_y[i]
            if 0<= next_x and next_x<n and 0<=next_y and next_y < m and visited[next_x][next_y] is False and road_list[next_x][next_y] == 1:
                visited[next_x][next_y] = visited[this_x][this_y] + 1
                queue.append((next_x,next_y))
    print(visited[n-1][m-1])

road_list = []
visited = [ [False for j in range(m)] for i in range(n)]
visited[0][0] = 1
for i in range(n):
    input_str = input()
    road_list.append([int(input_str[j]) for j in range(m)])


bfs()