import sys
input = sys.stdin.readline

def checkBfs(start):
    global check_list
    global edge_list

    check_list[start] = 0 
    queue = [start]

    while queue:
        this = queue.pop(0)

        for edge in edge_list[this]:
            if check_list[edge] is False:
                check_list[edge] = 0 if check_list[this] == 1 else 1
                queue.append(edge)
            else :
                if check_list[edge] == check_list[this]:
                    return False

    return True

case = int(input())

for _ in range(case):
    v,e = map(int,input().split())
    edge_list = [[] for __ in range(v)]
    check_list = [False for __ in range(v)]
    for i in range(e):
        start,end = map(int,input().split())
        edge_list[start-1].append(end-1)
        edge_list[end-1].append(start-1)
    
    for i in range(v):
        if (check_list[i] is  False):
            if checkBfs(i) is False:
                print('NO')
                break
        if i==v-1:
            print('YES')