import sys
input = sys.stdin.readline

n = int(input())
arr = [ int(_) for _ in input().split() ]

swap = False

for i in range(n-1,0,-1):
    if arr[i-1] > arr[i]:
        swap = i-1
        break

if swap is False :
    print(-1)
    sys.exit()


idx = arr.index(max([ _  for _ in arr[swap+1:] if _ < arr[swap]  ]))
# print(arr)
# print(idx)
arr[swap],arr[idx] = arr[idx],arr[swap]
arr[swap+1:] = sorted(arr[swap+1:],reverse=True) 
print(*arr)


# 4 3 2 1
# 4 3 1 2
# 4 2 3 1
# 4 2 1 3
# 4 1 3 2
# 4 1 2 3