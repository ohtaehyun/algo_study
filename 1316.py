N = int(input())
cnt = 0 
diff = ord('a')
for i in range(N):
    used_list = [ -1 for i in range(26)]
    word = input()
    latest_w = word[0]
    used_list[ord(word[0])- diff] = 0 
    for w in word: 
        if latest_w == w :
            pass
        else :
            latest_w = w 
            if used_list[ord(w) - diff ] == 0:
                break
            else :
                used_list[ord(w) - diff] = 0

    else:
        cnt+=1

print(cnt)
