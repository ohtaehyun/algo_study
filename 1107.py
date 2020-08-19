goal = int(input())
broken_len = int(input())
broken_list = [False] * 10
if broken_len > 0:
    for i in input().split():
        broken_list[int(i)] = True


def possible(n):
    global broken_list
    if n == '0' :
        return False if broken_list[0] else 1
    length = 0 
    n_list = list(map(int,n))
    for i in n_list:
        if broken_list[i] ==False :
            length+=1
        else:
            return False
    return length
result = abs(goal-100)
for i in range(1000001):
    r = possible(str(i))
    if r and result > abs(goal-i) + r:
        result = abs(goal-i) + r

print(result)



