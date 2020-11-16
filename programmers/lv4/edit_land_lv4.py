from itertools import chain
from collections import Counter 
def solution(land, P, Q):
    lands = list(chain.from_iterable(land))
    cnts =  Counter(lands)
    start = min(lands)
    end = max(lands)
    start = 1 if start == 0 else start 
    answer = 0
    while start == end :
        

    # lands = [] 
    # for l in land :
    #     lands += l 
    # cnts =  Counter(lands)
    # keys = cnts.keys()
    # start = min(keys)
    # end = max(keys)
    # start = 1 if start == 0 else start 
    # answer = -1
    # for j in range(start,end+1):
    #     cost = 0 
    #     for k in keys :
    #         if j - k > 0:
    #             cost += P*(j-k)*cnts[k]
    #         else :
    #             cost += Q*(k-j)*cnts[k]

    #     if answer == -1 or answer > cost:
    #         answer = cost

    return answer

print(solution([[4,4],[4,4]],3,2))