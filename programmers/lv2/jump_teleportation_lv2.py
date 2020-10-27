def solution(n):
    ans = 1
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else :
            n -= 1
            ans += 1
    return ans

print(solution(6))


# 5000 -> 2500 -> 1250 -> 625 ->  624 312 156 78 39  -> 38 19 -> 18 9 -> 8 4 2 1 ->0