N,K = map(int,input().split())
word_list = []

diff = ord('a')
# abcdefghijklmnopqrstuvwxyz
# 10100000100001000001000000 => 필수값

for i in range(N):
    input_str = input()
    word_value = 0
    for j in input_str :
        word_value |= ( 1<< ( ord(j) - diff))
    word_list.append(word_value)


def getCnt(mask):
    global word_list
    cnt = 0 
    for word in word_list:
        if word & ((1<<26)-1 -mask) == 0 :
            cnt+=1
    return cnt

def go(idx,learn_cnt,mask):
    global K
    if learn_cnt > K:
        return 0
    if idx == 26:
        return getCnt(mask)

    ans = 0
    # 단어를 배우는 경우
    tmp = go(idx+1, learn_cnt + 1 , mask | (1<<idx))
    if ans < tmp:
        ans = tmp
    
    # 필수단어는 무조건 배워야하니까 예외고 안은 배우지 않는 경우
    if idx != 0 and idx != 2 and idx != 8 and idx != 13 and idx != 19:
        # 배우지 않는 경우
        tmp = go(idx+1,learn_cnt,mask)
        if ans < tmp:
            ans = tmp

    return ans

print(go(0,0,0))