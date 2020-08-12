N = int(input())
arr = [0] 

for i in range(N):
    arr.append(int(input()))

memo = [ [0,0] for i in range(N+1)]
memo[1] = [0,arr[1]]
for i in range(2,N+1):
    memo[i][0] = memo[i-1][1]
    memo[i][1] = max(memo[i-2][1]+arr[i],memo[i-2][0]+arr[i-1]+arr[i])

print(memo[N][1])



# 1 0 1    
# 0 1 1