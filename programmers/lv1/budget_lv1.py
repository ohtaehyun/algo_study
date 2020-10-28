def solution(d, budget):
    d.sort()
    answer = 0

    for m in d:
        if budget >= d :
            budget -= d
            answer += 1
    return answer