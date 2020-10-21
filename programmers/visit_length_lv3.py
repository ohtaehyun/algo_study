def solution(dirs):
    visited = [[[-1] * 4 for i in range(11)]for j in range(11)]
    command = { 'U' : 0,'D' : 1,'R' : 2,'L' : 3}
    move = [[-1,0],[1,0],[0,1],[0,-1]]
    now_x = 5
    now_y = 5
    answer = 0
    for d in dirs:
        move_idx = command[d]
        nx,ny = move[move_idx]
        next_x,next_y = now_x+nx,now_y+ny
        if 0<= next_x < 11 and 0<= next_y < 11:
            if visited[next_x][next_y][move_idx] == -1 :
                answer+=1
                visited[next_x][next_y][move_idx] = 1
                move_idx = move_idx+1 if move_idx%2 == 0 else move_idx - 1
                visited[now_x][now_y][move_idx] = 1
                now_x,now_y =next_x,next_y
            else:
                now_x,now_y =next_x,next_y
    return answer

print(solution('UDUU'))