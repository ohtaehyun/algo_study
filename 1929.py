import sys 
input = sys.stdin.readline

m,n = map(int,input().split())

primes = []
visited = [ False for i in range(1,1000001)]
start = 2
while start <= n:
    if visited[start] == False:
        primes.append(start)
        j = start * 2
        while j <= n:
            visited[j] = True
            j+=start
    start +=1

for prime in primes:
    if prime >= m :
        print(prime)