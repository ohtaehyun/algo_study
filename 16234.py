import sys
from collections import deque
input = sys.stdin.readline

N,L,R = map(int,input().split())

people_list = []


for i in range(N):
    people_list.append(list(map(int,input().split())))


def find_union(x,y,visited):
    country_cnt = 1
    people_sum = people_list[x][y]
    diff_x = [ -1, 1, 0, 0 ]
    diff_y = [ 0, 0, -1, 1 ]
    queue = deque()
    queue.append((x,y))
    union = []
    while queue :
        now_x, now_y = queue.popleft()
        for i in range(4):
            next_x, next_y = now_x + diff_x[i] , now_y + diff_y[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if visited[next_x][next_y] == -1 and L <= abs(people_list[now_x][now_y] - people_list[next_x][next_y]) <= R :
                    visited[next_x][next_y] = 1 
                    queue.append((next_x,next_y))
                    union.append((next_x,next_y))
                    country_cnt += 1
                    people_sum += people_list[next_x][next_y]
    if union :
        union.append((x,y))
        return union, people_sum//country_cnt
    return False,False
count = 0
while True:
    visited = [ [-1 for j in range(N)] for i in range(N)]
    move_list = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 :
                visited[i][j] = 1 
                result,people = find_union(i,j,visited)
                if result :
                    move_list.append((result,people))
    if move_list:
        for countries,people in move_list :
            for x,y in countries:
                people_list[x][y] = people
        count += 1
    else :
        print(count)
        sys.exit()
                        
