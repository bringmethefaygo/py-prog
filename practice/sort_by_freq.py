
s = "acacacc"
d = {}
for char in s:
    d[char] = d.get(char,0)+1 
    # print(d)
        
sortedList = sorted(d.items(), key = lambda x:x[1])[::-1]
res = ''
# print(sortedList)

        
for tupleEle in sortedList:
    res = res+tupleEle[0]*tupleEle[1]
    # print(res)
print(res)
