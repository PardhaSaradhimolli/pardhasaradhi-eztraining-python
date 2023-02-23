dn=int(input("enter any binary number"))
bn=0
i=0
while dn!=0:
    r=dn%10
    bn=bn+r*(2**i)
    dn=dn//10
    i=i+1
    
print(bn)
#binary to decimal
