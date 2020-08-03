import sys
arr=[]
height_sum = 0
for i in range(0,9):
    n=int(input())
    arr.append(n)
    height_sum = height_sum + n
diff = height_sum - 100
arr = sorted(arr)
for i in range(0,8):
    for j in range(i+1,9):
        if arr[i] + arr[j] == diff:
            for k in range(0,9):
                if k != i and k != j:
                    print(arr[k]) 
            sys.exit()