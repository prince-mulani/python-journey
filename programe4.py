#count how many odd and even number
lst=[2,4,6,5,10,21,3,7,9]
odd =0
even=0
for num in lst:
    if num%2==0:
        even+=1
    else:
        odd+=1

print("odd:",odd)
print("even:",even)