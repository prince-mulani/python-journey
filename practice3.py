#example of local and globle variable
x=10      #globle
def test():
    x=5   #local
    print(x)

test()
print(x)
