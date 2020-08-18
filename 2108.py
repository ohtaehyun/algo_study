import sys
from collections import Counter
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(round(sum(arr)/N))
print(arr[(N-1)//2])
cnt = Counter(arr).most_common()
if len(cnt)>1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else :
    print(cnt[0][0])
print(arr[-1] - arr[0])