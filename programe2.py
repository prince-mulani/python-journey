#find second largest numberwithout using sort() and max()
lst=[10,32,89,21]
largest=lst[0]
second=lst[0]
for i in lst:
 
 if i>largest:
  second=largest
  largest=i
 elif i>second and i!=largest:
  second=i
print(second)
