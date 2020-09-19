N = int(input())
check_col = [True for i in range(N)]
check_digree_1 = [True for i in range(2*N-1)]
check_digree_2 = [True for i in range(2*N-1)]
def checkFalse(x,y):
    global check_col
    global check_digree_1
    global check_digree_2       

    if check_col[y] == False :
        return False

    if check_digree_1[x-y+N-1] == False :
        return False

    if check_digree_2 [x+y]== False:
        return False
    
    return True


def go(idx):
    global N
    global check_col
    global check_digree_1
    global check_digree_2       
    cnt = 0 
    if idx == N:
        return 1

    for i in range(N):
        if checkFalse(idx,i):
            check_col[i] = False
            check_digree_1[idx-i+N-1] = False
            check_digree_2 [idx+i] = False
            cnt += go(idx+1)
            check_col[i] = True
            check_digree_1[idx-i+N-1] = True
            check_digree_2 [idx+i] = True
    return cnt

print(go(0))