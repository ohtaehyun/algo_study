import sys
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = []

for i in range(n):
    matrix.append([int(_) for _ in input().split()])
sum_list = []
for i in range(n):
    for j in range(m):
        #  ㅡ 
        if j +3 < m:
            sum_list.append(sum(matrix[i][j:j+4]))
        # ㅣ
        if i + 3 < n:
            sum_list.append(sum([ matrix[_][j] for _ in range(i,i+4)  ]))
        #  ㅁ
        if i+1 < n and j+1 <m:
            s = matrix[i][j]+matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]
            sum_list.append(s)

        if i+2 < n and j+1 <m:
            s = matrix[i][j]+matrix[i+1][j]+matrix[i+2][j]+matrix[i+2][j+1]
            s1 = matrix[i][j]+matrix[i+1][j]+matrix[i+1][j+1]+matrix[i+2][j+1]
            s2 = matrix[i][j]+matrix[i+1][j]+matrix[i+2][j]+matrix[i+1][j+1]
            s3 = matrix[i][j]+matrix[i][j+1]+matrix[i+1][j+1]+matrix[i+2][j+1]
            sum_list.append(s)
            sum_list.append(s1)
            sum_list.append(s2)
            sum_list.append(s3)
            

        if i+2 < n and j-1 > -1 :
            s = matrix[i][j]+matrix[i+1][j]+matrix[i+2][j]+matrix[i+2][j-1]
            s1 = matrix[i][j]+matrix[i][j-1]+matrix[i+1][j-1]+matrix[i+2][j-1]
            s2 = matrix[i][j]+matrix[i+1][j]+matrix[i+1][j-1]+matrix[i+2][j-1]
            s3 = matrix[i][j]+matrix[i+1][j]+matrix[i+2][j]+matrix[i+1][j-1]
            sum_list.append(s)
            sum_list.append(s1)
            sum_list.append(s2)
            sum_list.append(s3)

        if i+1 < n and j+2 < m :
            s = matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i+1][j+2]
            s1 = matrix[i][j]+matrix[i+1][j]+matrix[i+1][j+1]+matrix[i+1][j+2]
            s2 = matrix[i][j]+matrix[i][j+1]+matrix[i+1][j+1]+matrix[i+1][j+2]
            s3 = matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i+1][j+1]
            sum_list.append(s)
            sum_list.append(s1)
            sum_list.append(s2)
            sum_list.append(s3)
        
        if i-1 > -1 and j+2 < m :
            s = matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i-1][j+2]
            s1 = matrix[i][j]+matrix[i-1][j]+matrix[i-1][j+1]+matrix[i-1][j+2]
            s2 = matrix[i][j]+matrix[i][j+1]+matrix[i-1][j+1]+matrix[i-1][j+2]
            s3 = matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i-1][j+1]
            sum_list.append(s)
            sum_list.append(s1)
            sum_list.append(s2)
            sum_list.append(s3)
        
            

print(max(sum_list))