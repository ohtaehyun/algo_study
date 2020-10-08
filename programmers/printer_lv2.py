def solution(priorities, location):
    answer = 1
    while priorities :
        now = priorities.pop(0)
        location -= 1
        if priorities and now < max(priorities) :
            priorities.append(now)
            if location == -1:
                location = len(priorities)-1
        else :
            if location == -1:
                break                
            answer+=1

    return answer
print(solution(	[1, 1, 9, 1, 1, 1], 0))