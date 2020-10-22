from collections import deque
def solution(N, road, K):
    answer = 0
    
    edges = [ [False] * N for i in range(N)]
    for r in road:
        f,t,cost =r
        f -= 1
        t -= 1
        if edges[f][t] is False or cost < edges[f][t] :
            edges[f][t] = cost
            edges[t][f] = cost
        
    visited = [-1 for i in range(N)]
    visited[0] = 0
    queue = deque([0])

    while queue :
        now = queue.popleft()
        now_cost = visited[now]
        next_edges = edges[now]
        for idx,cost in enumerate(next_edges):
            if cost is False :
                continue 
            next_cost = now_cost + cost
            if next_cost > K:
                continue
            if visited[idx] == -1 or next_cost < visited[idx]:
                queue.append(idx)
                visited[idx] = next_cost 
    
    for cost in visited:
        if cost != -1:
            answer+=1 

    return answer

print(solution(5,	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],	3))