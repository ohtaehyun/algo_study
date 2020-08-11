N,M = map(int,input().split())
nums = [i for i in range(1,N+1)]
check = []


def find(idx):
    global N
    global M
    global nums
    global check
    
    if len(check) == M:
        print(*check)
        return

    if idx < N:
        for i in nums :
            if i not in check:
                check.append(i)
                find(idx+1)
                check.pop()
find(0)