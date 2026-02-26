lst=[1,2,2,3,4,4,5]
l=[]
for i in lst:
    if i not in l:
        l.append(i)

print(l)