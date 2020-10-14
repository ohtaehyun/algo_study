from collections import deque

def solution(name):
    length = len(name)
    start = ord('A')
    end = ord('Z')
    queue = deque([(ord(name[0]),0)]) 
    answer = 0
    visited = [ -1 for i in range(len(name))]
    visited[0] = 1
    while queue:
        goal,now_idx = queue.popleft()
        answer += min([goal - start , end - goal + 1]) # 위아래 계산 
        
        for i in range(1,length): # 다음 좌우 계산
            r_idxs = now_idx + i if now_idx + i< length else now_idx + i - length 
            l_idxs = now_idx - i if now_idx-i >= 0 else now_idx - i + length
            if name[r_idxs] != 'A' and visited[r_idxs] == -1:
                visited[r_idxs] = 1
                queue.append((ord(name[r_idxs]),r_idxs))
                answer += i
                break
            elif name[l_idxs] != 'A' and visited[l_idxs] == -1:
                visited[l_idxs] = 1
                queue.append((ord(name[l_idxs]),l_idxs))
                answer += i
                break
    return answer
print(solution('JAN'))