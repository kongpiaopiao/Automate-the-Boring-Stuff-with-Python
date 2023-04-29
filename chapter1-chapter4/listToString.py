def listToString(lis):

    if len(lis)>1:
        liststring=lis[0]
        for i in range(1,(len(lis))):
            if i!=len(lis)-1:
                liststring=liststring+','+' '+lis[i]
            else:
                liststring=liststring+' '+'and'+' '+lis[i]
        print(liststring)
    else:
        print("This is an empty list!")

spam = ['cat', 'bat', 'rat', 'elephant']
listToString(spam)

