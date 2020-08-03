case = int(input())
memo = [0,1,2,4]
for _ in range(case):
    n =int(input())
    length = len(memo)
    if length < n+1:
        for i in range(length,n+1):
            memo.append(sum(memo[-3:]))
    print(memo[n])