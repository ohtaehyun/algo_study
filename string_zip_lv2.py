def solution(s):
    length = len(s)
    answer = length

    for i in range(1,length+1):
        cnt = 1
        result_str = ''
        before_str = ''
        for j in range(0,length,i):
            if j == 0 :
                before_str = s[j:j+i]
            elif before_str == s[j:j+i]:
                before_str = s[j:j+i]
                cnt+=1
            else :
                result_str += str(cnt) + before_str if cnt > 1 else before_str
                before_str = s[j:j+i]
                cnt=1     
        result_str += str(cnt) + before_str if cnt > 1 else before_str
        if len(result_str) < answer :
            answer = len(result_str)
    return answer



print(solution('xababcdcdababcdcd'))