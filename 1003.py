N = int(input())
memo = [(1,0),(0,1)]

for i in range(2,41):
    z,o = memo[i-2]
    z1,o1 = memo[i-1]
    memo.append((z+z1,o+o1))

for i in range(N):
    idx = int(input())
    print(*memo[idx])
