def solution(prices):
    length = len(prices)
    answer = [-1 for i in range(length)]
    for i in range(length):
        price = prices[i]
        for j in range(i+1,length):
            new_price = prices[j]
            if price>new_price:
                answer[i] = j-i
                break
        if answer[i] == -1 :
            answer[i] = length-1-i
            
        
    return answer