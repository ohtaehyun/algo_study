def solution(skill, skill_trees):
    s_list = [ i for i in skill]
    answer = 0
    for st in skill_trees:
        removed_st = ''.join([s for s in st if s in s_list])
        length = len(removed_st)
        if skill[:length] == removed_st:
            answer += 1
    return answer    
print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))