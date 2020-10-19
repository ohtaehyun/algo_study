def solution(clothes):
    dct = dict()
    for _ , clothe_type in clothes:
        if clothe_type in dct :
            dct[clothe_type] += 1
        else :
            dct[clothe_type] = 1
    answer = 1
    for item in dct.items():
        answer*=(item[1] + 1)
    return answer-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])