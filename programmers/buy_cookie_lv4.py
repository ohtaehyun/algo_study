def solution(cookie):
    length = len(cookie)
    answer = 0

    for i in range(length-1):
        front_sum = cookie[i]
        front_idx = i
        rear_sum = cookie[i+1]
        rear_idx = i+1
        while True:
            if front_sum == rear_sum and answer < front_sum:
                answer = front_sum

            if front_sum < rear_sum and 0 < front_idx :
                front_idx -= 1
                front_sum += cookie[front_idx]
            elif rear_sum < front_sum and rear_idx < length-1:
                rear_idx += 1
                rear_sum += cookie[rear_idx]
            else :
                break
    return answer
print(solution([1,1,1,3,1]	))