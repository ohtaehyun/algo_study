import sys
N = int(input())
line_list =  [False] * 501
lis = [] 
for _ in range(N):
    idx,to = map(int,sys.stdin.readline().split())
    line_list[idx] = to 

for i in range(1,501):
    if line_list[i] != False :
        if len(lis) == 0 or lis[-1] < line_list[i]:
            lis.append(line_list[i]) 
        else :
            for j in range(0,len(lis)):
                if lis[j] > line_list[i] :
                    lis[j] = line_list[i]
                    break

print(N-len(lis))
