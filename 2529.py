k = int(input())

inequeal_signs = [i for i in input().split()]
nums = [False ]*10

max_result = False
min_result = False

def find(prev,idx):
    global k
    global inequeal_signs
    global nums
        
    max_result = False
    min_result = False


    if idx == k :
        return str(prev),str(prev)

    equal_sign = inequeal_signs[idx]

    if equal_sign == '<':
        for i in range(prev+1,10):
            if nums[i] is True :
                pass
            else :
                nums[i] = True
                ma,mi = find(i,idx+1)
                nums[i] = False 
                if ma is not False and (max_result is False or int(ma) > int(max_result)):
                    max_result = ma
                if mi is not False and (min_result is False or int(mi) < int(min_result)):
                    min_result = mi
    else :
        for i in range(0,prev):
            if nums[i] is True :
                pass
            else :
                nums[i] = True
                ma,mi = find(i,idx+1)
                nums[i] = False 
                if ma is not False and (max_result is False or int(ma) > int(max_result)):
                    max_result = ma
                if mi is not False and (min_result is False or int(mi) < int(min_result)):
                    min_result = mi

    if max_result is not False :
        max_result = str(prev) + str(max_result)
    if min_result is not False :
        min_result = str(prev) + str(min_result)

    return max_result,min_result


for i in range(10):
    nums[i] = True
    ma,mi = find(i,0)
    if ma is not False and (max_result is False or int(ma) > int(max_result)):
        max_result = ma
    if mi is not False and (min_result is False or int(mi) < int(min_result)):
        min_result = mi
    nums[i]=False

print(max_result)
print(min_result)