n = int(input())
ps_arr = [0] + list(map(int,input().split()))

memo = [0]

for i in range(1,n+1):
    memo.append(min([memo[j]+ps_arr[i-j] for j in range(i)]))

print(memo[n])