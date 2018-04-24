list1 = []
n = int(input())
i =0 
for i in range(n):
    com = str(input())
    if(com == "insert"):
        i = int(input())
        e = int(input())
        list1.insert(i,e)
    elif(com == "print"):
        print(list1)
    elif(com == "remove"):
        e = int(input())
        list1.remove(e)
    elif (com == "append"):
        e = int(input())
        list1.append(e)
    elif (com == "sort"):
        list1.sort()
    elif (com == "pop"):
        list1.pop()
    elif (com == " reverse"):
        list1.reverse()
    
        
        
    
