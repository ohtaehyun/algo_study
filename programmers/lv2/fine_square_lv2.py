def getGcd(a,b):
    if a<b:
        b,a = a,b
    r = a % b
    if r == 0:
        return b    
    return getGcd(b,r)

def solution(w,h):
    gcd = getGcd(w,h)
    return w*h - (w+h-gcd)

print(solution(2,5))
