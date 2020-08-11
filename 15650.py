N,M = map(int,input().split())
nums = [ i for i in range(1,N+1)]
check = []
def find(idx):
    global N
    global M
    global nums
    if len(check ) == M :
        print(*check)

    for i in nums:
        if i not in check and (len(check) == 0 or i > check[-1]):
            check.append(i)
            find(idx+i)
            check.pop()
find(0)

