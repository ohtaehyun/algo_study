n =int(input())

memo = [0,0,1,1]

for i in range(4,n+1):
    next_list =[ memo[i-1]+1]

    if i %2 == 0:
        next_list.append(memo[int(i/2)] + 1)
    
    if i % 3 == 0:
        next_list.append(memo[int(i/3)]+1)

    memo.append(min(next_list))
print(memo[n])