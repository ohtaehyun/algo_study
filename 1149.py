import sys

n = int(input())
values = []
for i in range(n):
    values.append([ int (i) for i in sys.stdin.readline().split()])
memo = [[0,0,0] for i in range(n)]
memo[0] = values[0]

for i in range(1,n):
    for j in range(3):
        memo[i][j] = min ( [memo[i-1][k] + values[i][j] for k in range(3) if k != j])

print(min(memo[n-1]))