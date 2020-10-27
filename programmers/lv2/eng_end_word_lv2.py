def solution(n, words):
    last = words[0][-1]
    used = set()
    used.add(words[0])
    for i in range(1,len(words)):
        if words[i][0] != last or words[i] in  used:
            return [i%n +1 , i//n + 1]
        else :
            last = words[i][-1]
            used.add(words[i])
    return [0,0]