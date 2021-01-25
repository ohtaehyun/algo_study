def solution(a):
    answer = 2
    if len(a) <= 2:
        return len(a)
    escaped_nums = [0 for i in range(len(a))]
    left_min = a[0]
    right_min = a[-1]

    for i in range(1,len(a)-1):
        if a[i] < left_min :
            left_min = a[i]
            answer += 1
            escaped_nums[i] = 1
    for i in range(len(a)-1,0,-1):
        if a[i] < right_min:
            right_min = a[i]
            if escaped_nums[i] == 0 :
                answer += 1
        
    return answer

if __name__ == "__main__":
    print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))