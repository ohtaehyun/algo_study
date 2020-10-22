from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    p =deque(list(people))
    while p :
        weight = p.popleft()
        remain_weight = limit - weight
        while p :
            w = p.pop()
            if w <= remain_weight:
                break
            else :
                answer += 1
        answer += 1
    return answer
