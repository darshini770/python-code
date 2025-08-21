num=int(input("enter the number to check:"))
org=num
res=0
while(num0):
    rem=num%10
    res=res+pow(rem,3)
    num=num//10
if(res==org):
    print("the given number %d is armstrong number"%(org))
else:
    print("the number is not an armstrong number")
