from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque()
    total_weight = 0
    while queue or truck_weights:
        answer+=1
        if queue :
            for i in range(len(queue)):
                queue[i] = (queue[i][0],queue[i][1] + 1)
                
            if queue[0][1] >= bridge_length :
                w = queue.popleft()[0]
                total_weight -= w
    
        if truck_weights and truck_weights[0] + total_weight <= weight:
            queue.append((truck_weights[0],0))
            total_weight += truck_weights[0]
            truck_weights.pop(0)
    return answer