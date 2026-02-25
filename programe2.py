number=[]
for i in range(5):
   num= int(input("enter the number:"))
   number.append(num)

total = 0
for n in number:
   total=total + n


print(number)
print("sum",total)

