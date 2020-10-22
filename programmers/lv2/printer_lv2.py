def solution(priorities, location):
    answer = 0
    while priorities :
        now = priorities.pop(0)
        location -= 1
        if priorities and now < max(priorities) :
            priorities.append(now)
            if location == -1:
                location = len(priorities)-1
        else :
            answer+=1
            if location == -1:
                break                

    return answer
print(solution(	[1, 1, 9, 1, 1, 1], 0))