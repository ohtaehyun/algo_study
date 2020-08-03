import sys
input = sys.stdin.readline

now,goal = map(int,input().split())

distance = [False for _ in range(100001)]
distance[now] = 0

queue = [now]
next_queue = []

while queue:
    position = queue.pop(0)
    if 0 != position and 2*position <= 100000 and distance[position*2] is False:
        distance[position*2] = distance[position]
        queue.append(position*2)
    
    if 0 < position and distance[position-1] is False:
        distance[position-1] = distance[position]+1
        next_queue.append(position-1)
    
    if position <100000 and distance[position+1] is False:
        distance[position+1] = distance[position]+1
        next_queue.append(position+1)
    
    if not queue:
        queue=next_queue

print(distance[goal])


    