import sys
input = sys.stdin.readline

def merge_sort(unsorted_list,length):
    if length == 1:
        return unsorted_list
    middle = length//2
    left_list = merge_sort(unsorted_list[0:middle],middle)
    right_list = merge_sort(unsorted_list[middle:],length-middle)
    
    return merge(left_list,right_list,middle,length - middle)

def merge(left_list,right_list,left_length,right_length):
    merged_list = []
    l = 0 
    r = 0

    while l < left_length and r < right_length:
        if left_list[l] < right_list[r]:
            merged_list.append(left_list[l])
            l+=1
        else:
            merged_list.append(right_list[r])
            r+=1
    while l < left_length:
        merged_list.append(left_list[l])
        l+=1
    while r<right_length:
        merged_list.append(right_list[r])
        r+=1
    return merged_list 

n = int(input())
unsorted_list = [] 

for i in range(n):
    unsorted_list.append(int(input()))

sorted_list = merge_sort(unsorted_list,n)
for item in sorted_list:
    print(item)