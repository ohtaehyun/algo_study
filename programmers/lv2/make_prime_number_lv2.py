from itertools import combinations

def getPrimes():
    primes = [ True for i in range(3001)]
    primes[0] = False
    primes[1] = False
    i = 2 
    while i**2 < 3000:
        if primes[i] is True:
            j = 2
            while j*i < 3000:
                primes[j*i] = False
                j+=1
        i+=1

    return primes



def solution(nums):
    answer = 0
    primes = getPrimes()
    combs = combinations(nums,3)
    for c in combs :
        if primes[sum(c)] is True:
            answer+=1
    return answer

print(solution([1,2,7,6,4]	))