def solution(n, stations, w):
    lengths = []
    start = 1
    for s in stations:
        if s-w-start>0:
            lengths.append(s-w-start)
        start = s+w+1
    if start <= n:
        lengths.append(n-start+1)
    answer = 0
    for l in lengths:
        q,r = divmod(l,2*w+1)
        if r :
            q+=1
        answer += q
    return answer
# 1 2 |3 4 5| 6 7 8 9 |10 11 12| 13 14 15
print(solution(	4, [2], 1))