#create function that takes a 2D list and return sum of all element
def sum_2D_list(matrix):
    total=0
    for r in matrix:
        for element in r:
            total+=element
    return total

matrix=[]

rows=int(input("enter the number of row:"))
cols=int(input("enter the number of colomn:"))

for i in range(rows):
    temp_row=[]
    for j in range(cols):
        num=int(input())
        temp_row.append(num)
    matrix.append(temp_row)
for r in matrix:
        print(r)
print(sum_2D_list(matrix))