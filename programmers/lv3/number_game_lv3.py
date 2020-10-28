def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    length = len(B)
    b_start = 0
    for a in A:
        for i in range(b_start,length):
            b = B[i]
            b_start += 1
            if b>a :
                answer+=1
                break
    return answer