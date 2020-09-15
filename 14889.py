import math
import itertools

N = int(input())
arr = []

for i in range(N):
    arr.append([int(i) for i in input().split()])

def get_diff(combination):
    global arr
    global N
    used = [ True  if i in combination else False for i in range(N)]
    sum_start = 0 
    sum_link = 0 
    for i in range(N):
        for j in range(N):
            if(i != j):
                if used[i] is True and used[j] is True:
                    sum_start += arr[i][j]
                    
                elif used[i] is False and used[j] is False:
                    sum_link += arr[i][j]


    result = abs(sum_link - sum_start)
    if result == 0 :
        print(0)
        exit()
    return result

peoples = [i for i in range(N)]
combis = itertools.combinations(peoples,N//2)
ans = math.inf

for c in combis:
    result = get_diff(c)
    if result <  ans :
        ans = result
print(ans)