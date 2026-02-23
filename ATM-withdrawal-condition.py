balance =10000
correct_pin =1234

pin=int(input("enter your pin:"))

if pin==correct_pin:
    print("wellcome:")
    withdraw=int(input("enter the withdraw amount:"))
    if withdraw < 0:
        print("invalid amount")
    elif withdraw<=balance:
        print("Transaction successful")
        print("remaing balance:",balance-withdraw)
    else:
        print("invalid amount")
else:
    print("invalid pin")