N = int(input())
T = []
P = []
def Calc (day,total):
    global T
    global P
    global N
    result1 = total
    result2 = total
    if day >= N:
        return total
    if day < N-1:
        result2 = Calc(day+1,total)

    if day + T[day] <= N :
        result1 = Calc(day+T[day],total+P[day])
    return max([result1,result2])
for i in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

print(Calc(0,0))