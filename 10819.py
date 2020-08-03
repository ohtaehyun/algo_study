import sys
input =sys.stdin.readline

def next_permutations(arr,n):
    swap = False 

    for i in range(n-1,0,-1):
        if arr[i-1] < arr[i]:
            swap = i-1
            break
    
    if swap is False:
        return False

    swap2 = n-1
    while arr[swap2] <= arr[swap]:
        swap2 -= 1

    arr[swap],arr[swap2] = arr[swap2],arr[swap]
    arr[swap+1:] = reversed(arr[swap+1:])  
    ans = 0
    for i in range(1, n):
        ans += abs(arr[i]-arr[i-1])
    return ans


n = int(input())
arr = [int(_) for _ in input().split()]
arr=sorted(arr)
max_value = sum([ abs(arr[i] - arr[i+1]) for i in range(0,n-1)])
while True:
    result = next_permutations(arr,n)
    if result is False:
        break
    max_value = max(max_value,result)
print(max_value)
