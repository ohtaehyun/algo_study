N,M = map(int,input().split())
nums = [i for i in range(1,N+1)]
result = []
def find(length):
    global N
    global M
    global nums
    global result

    if length == M :
        print(*result)
        return

    for idx in nums:
        result.append(idx)
        find(length + 1)
        result.pop()


find(0)