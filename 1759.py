L,C = map(int,input().split())

alpha_list = input().split()
alpha_list.sort()
def find(alpha,idx,cnt,result):
    if cnt == L :
        m_length =len( [ result[i] for i in range(L) if result[i]  in ['a','e','i','o','u']])

        if m_length > 0 and L-m_length > 1:
            print(result)

    elif cnt < L and idx < C:
        find(alpha_list,idx+1,cnt+1,result+alpha_list[idx])
        find(alpha_list,idx+1,cnt,result)
    

find(alpha_list,0,0,'')
# a c i s t w