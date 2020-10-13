from collections import deque
def solution(n):
    answer = []
    if n == 1:
        return [1]
        
    for i in range(1,n+1):
        answer.append([-1 for j in range(i)])
    
    move_queue = deque([[0,1],[-1,-1]])
    move_x,move_y = 1,0 # 아래로 먼저
    queue = deque()
    queue.append([0,0])
    answer[0][0] = 1
    num = 2
    while queue:
        now_x,now_y = queue.popleft()
        next_x , next_y = now_x + move_x, now_y + move_y

        if not (0 <= next_x < n and 0 <= next_y < next_x + 1) or answer[next_x][next_y] != -1:
            move_queue.append([move_x,move_y])
            move_x, move_y = move_queue.popleft()
            next_x , next_y = now_x + move_x, now_y + move_y
        if answer[next_x][next_y] == -1:
            answer[next_x][next_y] = num 
            num += 1
            queue.append([next_x,next_y])
    result = []
    for a in answer:
        result += a
    return result


print(solution(1))