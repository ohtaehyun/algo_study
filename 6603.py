import sys 
input = sys.stdin.readline
def print_perm(p_arr,arr):
    print_arr = []
    for i in range(len(p_arr)):
        if p_arr[i] == 1:
            print_arr.append(arr[i+1])
    print(*print_arr)


def next_perm(p_arr ):
    i = len(p_arr) - 1
    while i > 0 and p_arr[i-1] >= p_arr[i]:
        i =- 1
    if i < 0:
        return False 
    j = len(p_arr) -1 
    while p_arr[i] >= p_arr[j]:
        j =- 1

    p_arr[i],p_arr[j] = p_arr[j],p_arr[i]

    j = len(p_arr) -1 
    while i+1 != j:
        p_arr[i+1],p_arr[j] = p_arr[j],p_arr[i+1]
        i =+ 1
        j =+ 1
    return True

while True:
    arr = [int(_) for _ in input().split()]
    if len(arr) == 1 :
        sys.exit()
    p_arr = [0 for _ in range(arr[0])]
    for i in range(arr[0]-1,arr[0]-7,-1):
        p_arr[i] = 1
    print_perm(p_arr,arr)

    while next_perm(p_arr):
        print_perm(p_arr,arr)
        