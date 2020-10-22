def solution(sticker):
    length = len(sticker)
    memo1 = [0 for i in range(length)]
    memo2 = [0 for i in range(length)]
    memo1[0] = 0
    memo1[1] = sticker[1]
    memo2[0] = sticker[0]
    memo2[1] = sticker[0] 
    for i in range(2,length-1):
        memo1[i] = max([memo1[i-2]+sticker[i],memo1[i-1]])
        memo2[i] = max([memo2[i-2]+sticker[i],memo2[i-1]])
    
    memo1[length-1] = max([memo1[length-3]+sticker[length-1],memo1[length-2]])

    return max([memo1[length-1],memo1[length-2],memo2[length-1],memo2[length-2]])

print(solution([1, 3, 2, 5, 4]))