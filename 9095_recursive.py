n = int(input())

def getCount(goal,total):
    cnt=0
    if goal == total :
        return 1
    diff = goal - total
    
    for i in range(1,4):
        if diff>= i:
            cnt = cnt + getCount(goal,total+i)
    return cnt


for i in range(n):
    goal = int(input())
    print(getCount(goal,0))