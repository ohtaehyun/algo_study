N,M = map(int,input().split())
arr = [int(i) for i in input().split()]

arr.sort()
check = [] 
def find(length):
    global M
    global arr
    global check 
    if length == M:
        print(*check)
        return
    for i in arr:
        if i not in check:
            check.append(i)
            find(length + 1)
            check.pop()

find(0)