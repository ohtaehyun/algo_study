arr = [ int(i) for i in input()]

arr.sort(reverse=True)

s = ''
for i in arr:
    s += str(i)
print(s)