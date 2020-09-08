N = int(input())

word_dict = {}

for i in range(N):
    word = input()
    length = len(word)

    for i in range(length):
        if word[i] in word_dict:
            word_dict[word[i]] += 10**(length-1-i)
        else:
            word_dict[word[i]] = 10**(length-1-i)

values = [ int(v) for k,v in word_dict.items()]
values.sort(reverse=True)
weight = 9
ans = 0 
for value in values:
    ans = ans + value * weight
    weight -= 1

print(ans)