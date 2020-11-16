croatia_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
length = len(word)
cnt = 0
i = 0
while i < length :
    if i+2 < length:
        w = word[i:i+3]
        w2 = word[i:i+2]
        if w in croatia_list :
            cnt +=1
            i+=3
        elif w2 in croatia_list:
            cnt +=1
            i+=2
        else :
            cnt+=1
            i+=1
    elif i+1 < length:
        w = word[i:i+2]
        if w in croatia_list :
            cnt +=1
            i += 2
        else :
            cnt+=1
            i+=1
    else :
        cnt+=1
        i+=1
print(cnt)