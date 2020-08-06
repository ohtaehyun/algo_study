N,M = map(int,input().split())
arr = [int(i) for i in input().split()]
cnt = 0 
for i in range(1,(1<<N)):
    total = sum(arr[j] for j in range(N) if i&(1<<j) > 0)
    if total == M:
        cnt += 1

print(cnt)