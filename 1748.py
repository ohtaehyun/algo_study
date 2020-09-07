N = int(input())
# if N < 10:
#     print(N)
#     exit()
# 1 ~ 9 : 9 
# 10 99 : 90
# 100 999 : 900

start = 9
flag = 1
ans = 0

while N > ((10**flag)-1) :
    ans += start * flag
    start *= 10
    flag+=1

ans += (N-(start//9)+1) * flag
print(ans)