def find(num_list,idx,length,result):
    if len(result) == 6:
        print(*result)
    elif idx<length :
        result.append(num_list[idx])
        find(num_list,idx+1,length,result.copy())
        result.pop()
        find(num_list,idx+1,length,result.copy())


while True:
    input_list = [ int(i) for i in input().split()]
    n = input_list[0]
    if n == 0 :
        break
    lotto_nums = input_list[1:]
    lotto_nums.sort()
    find(lotto_nums,0,n,[])
    print()