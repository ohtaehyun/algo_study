import sys
input = sys.stdin.readline

n = int(input())
arr = [int(i) for i in input().split()]

swap_x = False
for i in range(n-1,0,-1):
    if arr[i-1] <= arr[i]:
        swap_x = i-1
        break

if swap_x is False:
    print(-1)
    sys.exit()

# for idx , num in enumerate(arr):

idx = arr.index(min ( [ _ for _ in arr[swap_x+1:] if _ > arr[swap_x]]))


arr[swap_x],arr[idx] = arr[idx],arr[swap_x]

arr[swap_x+1:] = sorted(arr[swap_x+1:])
# sorted(arr[swap_x+1:] , reverse=True)

print(*arr)

# 5 2 3 4 1
# 5 2 4 1 3