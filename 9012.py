N = int(input())

for i in range(N):
    vps = input()
    cnt = 0 
    for v in vps:
        if v == '(':
            cnt += 1
        else :
            cnt -= 1
        
        if cnt < 0 :
            print('NO')
            break
    else:
        if cnt != 0 :
            print('NO')
        else :
            print('YES')