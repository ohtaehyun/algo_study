def solution(number, k):
    cnt = 0 
    fixed_str = ''
    while cnt < k :
        if len(number) == k-cnt:
            number = ''
            break
        max_num = -1
        max_idx = -1
        for idx,i in enumerate(number[0:k-cnt+1]):
            if max_num < int(i):
                max_num = int(i) 
                max_idx = idx
            if i == '9':
                break
        cnt+=max_idx
        fixed_str += str(max_num)
        number = number[max_idx+1:]

    return fixed_str+number

print(solution(	"4177252841", 4))

