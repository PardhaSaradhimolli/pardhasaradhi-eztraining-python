n=int(input("enter the weight"))
i=0
if n==0:
    print("Zero time")
if n>7000:
    print("Invalid input")

if n<=2000 and n>0:
    print("the estimated time  =25")
elif n<=4000 and n>2001:
    print("the estimated time =35")

elif n<=7000 and n>=4001:
    print("the estimated time= 45")
    
