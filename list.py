list1 = [1,2,3,4,5,6,7,8,9,10]
print("no of memebers in the list=",list1)
print(len(list1))
print(list1[1:6:1])
print(list1[1:])
print(list1[:9])
print(list1[:-4])
print(list1[-1: :-1])
a = len(list1)
positive =0
while(positive<a):
    print("list1[",positive,"]=",list1[positive])
    positive+=1
negative = -a
print("***************************************")
while(negative<=(-1)):
    print("list1[",negative,"]=",list1[negative])
    negative +=1
list2 = [None,None ,None,None]
print(list2)
list3 = [ 1,3,5]
list4 = [6,8,9]
print("summation = ",list3 + list4)
print("MULTIPLICATION=",list3*3)
print("MINIMUM NO IN THE LIST3 AND LIST4 = ", min(list3),min(list4))
print("MAXIMUM NO IN THE LIST3 AND LIST4 = ",max(list3),max(list4))


letter = "BANK OF INDIA"
print(letter)
print(type(letter))
letter1 = list(letter)
print("LIST CREATED FROM THE STRING = ",letter1)
print(type(letter1))


print(list3 in list1)#false
print(list4 in list1)#false
print(letter1 in list3)# false
print(letter1 not in list4)# true
list5 = list1[3:9]
print(list5)
list1[1:9]= list2
print(list1)
print("no of memebers in the list=",len(list1))
del list3[2]
print(list3)
print()
list4[2] = 10
print(list4)
del list1[3]
print(list1)

list3.append(27)
print("the appended list :",list3)
index1 = list3.index(1)
print("ELEMENT AT THE INDEX 1 :",index1)
list3.extend([1,3,4,5,6,7,8,89])
print("LIST3 AFTER EXTENDED:",list3)
count1 =list3.count(1)
print("COUNT OF NUMBER 1 IN THE LIST IS :",count1)
list3.reverse()
print("THE REVERSE ORDER OF THE LIST:",list3)
list3.sort()
print("THE SORTED ORDER OF THE LIST:",list3)
list3.copy()
print(list3)
list3.remove(89)
print(list3)
list3.clear()
print("THE LIST IS CLEAR NOW :",list3)




















