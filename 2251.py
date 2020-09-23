from collections import deque
max_list = [ int(i) for i in input().split() ]
visited = [[[ False for i in range(max_list[2]+1)] for j in range(max_list[2]+1)] for k in range(max_list[2] + 1)]
visited[0][0][max_list[2]] = True
can_list = set()

queue = deque()
queue.append([0,0,max_list[2]])
#  a_cup=0 b_cup=1 c_cup=2
def move_water(from_cup , to_cup , water_list):
    for i in range(3):
        if i != from_cup and i != to_cup:
            the_other_cup = i
    movable_water =  water_list[from_cup]
    gettable_water = max_list[to_cup] - water_list[to_cup]
    moved_water = gettable_water if gettable_water < movable_water else movable_water
    result = [0 , 0 ,0]
    result[the_other_cup] = water_list[the_other_cup]
    result[from_cup] = water_list[from_cup] - moved_water
    result[to_cup] = water_list[to_cup] + moved_water
    return result
while queue:
    water_list = queue.popleft()
    if water_list[0] == 0 :
        can_list.add(water_list[2])

    for i in range(3):
        for j in range(3):
            if i != j :
                a,b,c = move_water(i,j,water_list)
                if visited[a][b][c] is False:
                    visited[a][b][c] = True
                    queue.append([a,b,c])

print(*sorted(can_list))