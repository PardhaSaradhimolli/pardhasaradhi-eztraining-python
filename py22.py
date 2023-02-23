n=int(input("enter the number"))
esum=0
osum=0
i=0
while (n!=0):
    r=n%10
    n=n//10
    
    if r%2==0:
        esum=esum+r
    
    elif r%2!=0:
        osum=osum+r
print("odd sum=",osum)
print("even sum=" ,esum)
dif=esum-osum
print(dif)
#sum of even digits and odd 
