def gcd(a,b):
    if(b>a):
        a,b = b,a 
    while b != 0:
        r = a%b 
        a = b
        b = r 
    return a 

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M,N,x,y = map(int,sys.stdin.readline().split())
    lcm = (M*N)/gcd(M,N) #두 최대값의 최소 공배수

    while True:
        if x > lcm:
            print(-1)
            break
        if (x-1) % N + 1 == y:
            print(x)
            break
        x += M 

