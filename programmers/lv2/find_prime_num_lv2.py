from itertools import permutations

def check(num_str):
    num = int(num_str)
    if num == 1:
        return False
    
    if num != 2 and num%2 == 0 :
        return False 
    
    for i in range(3,num,2):
        if num % i == 0 :
            return False
    
    return True
def solution(numbers):
    cnt = 0
    primes = set()
    length = len(numbers)
    for i in range(1,length + 1):
        pers = permutations(numbers,i)
        for p in pers:
            new_num = ''.join(p)
            if check(new_num):
                if int(new_num) not in primes:
                    primes.add(int(new_num))
                    cnt += 1          
    return cnt

print(solution('1234567'))