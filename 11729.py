N = int(input())

def move(from_idx,to_idx):
    print('{} {}'.format(from_idx,to_idx))

def hanoi(n,f,t,other):
    if n==1:
        move(f,t)
        return
    
    hanoi(n-1,f,other,t)
    move(f,t)
    hanoi(n-1,other,t,f)

print(2**N-1)
hanoi(N,1,3,2)