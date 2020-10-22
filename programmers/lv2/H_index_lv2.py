def solution(citations):
    length = len(citations)
    citations.sort()

    for idx,num in enumerate(citations):
        if length-idx <= num:
            return length-idx
    return 0


print(solution([1,1,1,2,6]))