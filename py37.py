word=str(input("enter the word"))
i=0
while(i<len(word)):
    letter=word[i]
    print(chr(ord(letter)+2))
    i+=1
