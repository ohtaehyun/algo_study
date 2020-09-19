N = int(input())
sum_str = input()
sum_list = [[False]*N for i in range(N)]
written_list = [False for i in range(N)]


def check_ans(idx):
    global N
    global sum_list
    global written_list
    sum_value = 0
    for i in range(idx,-1,-1):
        sum_value += written_list[i]
        flag = sum_list[i][idx]
        if flag == '+':
            if sum_value <= 0 :
                return False
        elif flag == '-':
            if sum_value >= 0 :
                return False
        else :
            if sum_value != 0 :
                return False
    return True

def go(idx):
    global N
    global sum_list
    global written_list

    if idx == N:
        return True

    flag = sum_list[idx][idx]

    if flag == '+':
        now_list = [ i for i in range(1,11)]
    elif flag == '-':
        now_list = [ i for i in range(-10,0)]
    else :
        now_list = [0]
    for now in now_list: 
        written_list[idx] = now
        if check_ans(idx):
            rslt = go(idx+1)
            if rslt is True:
                return True
    return False
    
idx = 0
for i in range(N):
    for j in range(i,N):
        sum_list[i][j] = sum_str[idx]
        idx+=1

go(0)
print(*written_list)