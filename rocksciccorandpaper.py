i=0
uscore=0
cscore=0
arr=["rock","paper","scissor"]
for i in range(0,5):
    uchoice=input("enter  your choice (rock,scissor,paper)").lower()
    if uchoice in arr:
        print( "your choice is",uchoice)
    elif uchoice not in arr:
        print("invalid input")
    import random
    cchoice=random.randint(0,2)
    cchoice=arr[cchoice]
    print( "computer choice is",cchoice)
    if uchoice==cchoice:
        print("draw")
    if uchoice=="rock" and cchoice=="scissor":
        print("user won")
        uscore
    elif uchoice=="paper" and cchoice=="rock":
        print("user won")
        uscore+=1
        
    elif uchoice=="scissor" and cchoice=="paper":
        print("user won")
        uscore+=1
    else :
        print("computer won")
        cscore+=1
print( "your score is",uscore)
print("computer score is ",cscore)
if uscore>cscore:
    print(" finally you won")
elif uscore<cscore:
    print("finally computer won")
else:
    print("Draw")
    


