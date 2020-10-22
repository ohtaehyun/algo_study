def divideString(p):
    if p == '':
        return ''

    l_cnt = 0
    r_cnt = 0 
    u = ''
    v = p
    is_u_perfect = True

    for c in p :
        if c == '(':
            l_cnt += 1

        elif c == ')':
            r_cnt += 1

        if r_cnt > l_cnt :
            is_u_perfect = False
            
        if l_cnt == r_cnt :
            u = p[0:l_cnt+r_cnt]
            v = p[l_cnt+r_cnt:]
            break
    if is_u_perfect :
        return u+divideString(v)
    else :
        new_str =''
        for c in u[1:-1]:
            new_str += '(' if c == ')' else ')'
        return '(' + divideString(v) + ')' + new_str

def solution(p):
    return divideString(p)

# print(solution("()))((()"))

print(solution("((()(())))"))