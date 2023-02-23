n=int(input("enter the number"))
i=0
sum=0
osum=0
while(i<=n):

    if i%2==0:
        sum=sum+i
    
    else:
        osum=osum+i
    i=i+1
print(sum)
print(osum)
#print sum of odd and even
