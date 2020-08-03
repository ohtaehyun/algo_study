n = int(input())
memo = [0,1,3]
for i in range(3,n+1):
    memo.append(((2*memo[i-2])%10007 + (memo[i-1])%10007)%10007)
print(memo[n])