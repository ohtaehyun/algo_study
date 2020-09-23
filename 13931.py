start,goal = map(int,input().split())
time_list = [False for _ in range(200001)]
time_list[start] = 0
route_list = ['' for _ in range(200001)]
route_list[start] = -1

q = []
q.append(start)

while q :
    this = q.pop(0)
    
    if this == goal:
        break
    now_time = time_list[this]
    if this*2 < 200000 and (time_list[this*2] is False or now_time + 1< time_list[this*2] ):
        time_list[this*2] = now_time + 1
        route_list[this*2] = this
        q.append(this*2)

    if this  > 0 and (time_list[this-1] is False or now_time + 1 < time_list[this-1] ):
        time_list[this-1] = now_time + 1
        route_list[this-1] =this
        q.append(this-1)

    if this < 200000 and(time_list[this+1] is False or now_time + 1 < time_list[this+1] ):
        time_list[this+1] = now_time + 1
        route_list[this+1] = this
        q.append(this+1)

print(time_list[goal])
route_result = [ 0 for i in range(time_list[goal]+1)]
idx = goal
for j in range(time_list[goal] , -1 , -1):
    route_result[j] = idx
    idx = route_list[idx]
print(*route_result)