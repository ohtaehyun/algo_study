import sys
N = int(input())
arr =[]
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
memo = [[0 for i in range(N)] for j in range(N)]
memo[0][0] = arr[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j == 0 :
            memo[i][j] = memo[i-1][j] + arr[i][j]
        elif j == i :
            memo [i][j] = memo[i-1][j-1] + arr[i][j]
        else :
            memo[i][j] = max(memo[i-1][j] + arr[i][j], memo[i-1][j-1] + arr[i][j])

print(max(memo[N-1]))