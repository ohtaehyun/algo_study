N,S = map(int,input().split())
nums = list(map(int,input().split()))

def count(nums,idx,length,goal,now):
    cnt = 0
    if goal == now and idx == length:
        cnt+=1
    if idx < length:
        cnt += count(nums,idx+1,length,goal,now+nums[idx])
        cnt += count(nums,idx+1,length,goal,now)
    return cnt
if S == 0 :
    print(count(nums,0,N,S,0)-1)
else:
    print(count(nums,0,N,S,0))
    