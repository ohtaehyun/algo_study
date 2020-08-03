
primes = []
visited = [False for _ in range(1,1000002)]
i = 2 
while i <= 1000000 :
    if visited[i] == False:
        primes.append(i)
        j=i*2 
        while j <= 1000000:
            visited[j] = True
            j=j+i
    i +=1 

while True:
    n = int(input())
    if n == 0 :
        break

    for prime in primes:
        if visited[ n-prime ] == False:
            print(str(n)+' = ' + str(prime) + ' + ' + str(n-prime))
            break
        
