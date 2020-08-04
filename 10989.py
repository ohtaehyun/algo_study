import sys
input = sys.stdin.readline

total =0
n = int(input())
count_arr = [ 0 for i in range(0,10001)]

for i in range(n):
    num = int(input())
    count_arr[num] += 1

for i in range(10001) :
    while count_arr[i] > 0:
        print(i)
        count_arr[i] -= 1