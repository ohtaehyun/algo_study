def solution(N, number):
    if N == number :
        return 1
    answer = 1
    dp = [set([N])]
    nStr = str(N)
    for i in range(8):
        nStr+= str(N)
        next_set = set()
        next_set.add(int(nStr)) 
        for j in range(i//2 + 1):
            for k in dp[j]:
                for l in dp[i-j]:
                    next_set.add(k+l)
                    next_set.add(k-l)
                    next_set.add(k*l)
                    if l != 0:
                        next_set.add(k//l)
                    if k != 0 :
                        next_set.add(l//k)
        dp.append(next_set)
        answer+=1
        if number in next_set:
            return answer
        
    return -1

if __name__ == "__main__":
    print(solution(2,11))