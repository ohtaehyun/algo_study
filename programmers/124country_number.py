def solution(n):
    numbers= '124'
    if n<4:
        return numbers[n%3-1]
    
    q,r = divmod(n-1,3)
    return solution(q) + numbers[r]


print(solution(15))