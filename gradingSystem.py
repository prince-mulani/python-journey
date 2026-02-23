mark = float(input("enter your mark:"))

if mark>=90:
    grade="A+"
elif mark>=80:
    grade="A"
elif mark>=70:
    grade="B"
elif mark>=60:
    grade="c"
elif mark>=50:
    grade="D"
else:
    grade="FAIL"

print("your grade is:",grade)