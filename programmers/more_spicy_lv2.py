import heapq 
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        print(scoville)
        spicy = heapq.heappop(scoville)
        if spicy >= K:
            return answer
        else :
            if scoville:
                heapq.heappush(scoville,spicy+2*heapq.heappop(scoville))
                answer+=1
            else :
                return -1

solution([1,2]	,7)