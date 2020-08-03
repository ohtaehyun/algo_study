n = int(input())
ps_list = [0] + list(map(int,input().split()))

memo = [0]

for i in range(1,n+1):
    memo.append(  max([ memo[j] + ps_list[i-j] for j in range(i) ]) )

print(memo[n])