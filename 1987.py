R,C = map(int,input().split())
diff = ord('A')

visited_list = [False for i in range(26)]
alpha_list = []
for i in range(R):
    alpha_list.append(input())
def check(position):
    global C
    global R
    global visited_list
    global diff
    global alpha_list

    x,y = position
    if x < 0 or y <0 or  x==R or y == C:
        return False
    alpha_idx = ord(alpha_list[x][y]) - diff
    if visited_list[alpha_idx] is True:
        return False 

    return True
def go(now_position):
    global alpha_list
    global visited_list
    global diff
    ans = 1
    cnt = 0
    x,y = now_position

    next_positions = [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]

    for position in next_positions:
        if check(position):
            n_x,n_y = position
            visited_list[ord(alpha_list[n_x][n_y])-diff] = True
            tmp = go(position)
            if cnt < tmp:
                cnt = tmp
            visited_list[ord(alpha_list[n_x][n_y])-diff] = False
    return ans + cnt

start_alphabet = alpha_list[0][0]
visited_list[ord(start_alphabet)-diff] = True
print(go((0,0)))