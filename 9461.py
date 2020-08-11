n = int(input())


memo = [1,1,1,2,2]
length = 5

for i in range(n):
    N = int(input())

    if N > length:
        for j in range(length-1,N):
            memo.append(memo[j]+memo[j-4])
            length+=1
    
    print(memo[N-1])