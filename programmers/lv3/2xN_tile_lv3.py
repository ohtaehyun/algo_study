def solution(n):
    a = [0,1,2]
    if n > 2 :
        for i in range(3,n+1):
            a.append((a[i-2] + a[i-1])%1000000007)
    return a[n]

if __name__ == "__main__":
    print(solution(16))