def solution(progresses, speeds):
    
    answer = []
    for p, s in zip(progresses,speeds):
        remain = 100 - p
        q,r = divmod(remain,s)
        if r > 0 :
            q+=1
        if len(answer) == 0 or answer[-1][0] < q:
            answer.append([q,1])
        else :
            answer[-1][1] += 1
        
    return [ ans[1] for ans in answer]

print(solution(	[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))