import sys 
input = sys.stdin.readline

def isPrime(num):
    if num < 2 :
        return False
    i =2
    while i*i <= num :
        if num%i == 0:
            return False
        i+=1
    return True

n = int(input())

arr = [int(_) for _ in input().split()]
cnt = 0
for num in arr :
    if isPrime(num) == True:
        cnt  += 1

print(cnt)