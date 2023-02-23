a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))
if a==b==c:
    print("three numbers are equal")
if a>b and a>c:
    print(a,"is the maximum of three")
elif b>a and b>c:
    print(b,"is the maximum of three")
else:
    print(c,"is the maximum of three")
#largest of three
