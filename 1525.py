from collections import deque
puzzle = [ ]
visited = dict()
start_value = 0
for i in range(3):
    input_str = input().split()
    for j in input_str:
        if j == '0' :
            j = '9'
        start_value = start_value * 10 + int(j)

visited[str(start_value)] = 0

queue = deque()
queue.append(start_value)

def swap(string,target1,target2):
    temp_list = list(string)
    temp_list[target1],temp_list[target2] = temp_list[target2],temp_list[target1]
    return ''.join(temp_list) 

while queue:
    now = str(queue.popleft())
    now_cnt = visited[now]
    if now == '123456789':
        print(visited[now])
        exit()
    zero_idx = str.index(str(now),'9')
    next_list = [3,-3]
    if zero_idx % 3 != 0 :
        next_list.append(-1)
    if zero_idx % 3 != 2 :
        next_list.append(1)
    swap_list = [ i + zero_idx for i in next_list if -1 < i+zero_idx and i+zero_idx < 9]
    for target in swap_list:
        key = swap(now,zero_idx,target)
        if key not in visited:
            visited[key] = now_cnt+1
            queue.append(key)
print(-1)