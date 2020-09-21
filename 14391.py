R,C = map(int,input().split())
arr = [[0 for i in range(C)]for j in range(R)]
for i in range(R):
    inp_str = input()
    for j in range(C):
        arr[i][j] = int(inp_str[j])

ans = 0 
i = 0
#  0 => 가로 1 => 세로
while i < (1<<(R*C)):
    sum_value = 0
    # 가로값 더하기
    for j in range(R):
        now = 0
        for k in range(C):
            bit_idx = j*C + k
            if i & (1<<bit_idx) == 0:
                now=now*10+arr[j][k]
            else:
                sum_value += now
                now = 0
        sum_value += now

    # 세로값 더하기
    for j in range(C):
        now = 0
        for k in range(R):
            bit_idx = k*C + j
            if i & (1<<bit_idx) != 0:
                now=now*10+arr[k][j]
            else:
                sum_value += now
                now = 0
        sum_value += now

    if ans<sum_value:
        ans=sum_value
    i+=1
print(ans)