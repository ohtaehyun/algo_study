N,M = map(int,input().split())
nums = [ i for i in range(1,N+1)]
check = []

def find(length,last):
    global N
    global M
    global nums 
    global check

    if length == M :
        print(*check)
        return

    for i in nums:
        if length == 0 or i >= last:
            check.append(i)
            find(length + 1,i)
            check.pop()

find(0,0)