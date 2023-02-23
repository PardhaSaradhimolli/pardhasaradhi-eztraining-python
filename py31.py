n=int(input("enter a number"))
s=r=0
while(n!=0):
    r=n%10
    s=s+(r*r*r)
    
    
    n=n//10
if s==n:
    print("number is armstrong")
