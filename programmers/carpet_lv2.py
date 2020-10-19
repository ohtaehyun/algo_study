def solution(brown, yellow):
    answer = []
    for r in range(3,brown//2):
        c = brown//2 -r + 2

        if r*c - brown == yellow :
            return[c,r]
    return answer


solution(10,2)