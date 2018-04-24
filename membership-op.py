a = "learn"
b = "learn python"
ans1 = a in b
ans2 = a not in b
ans3 = b in a
ans4 = b not in a
print("a in b = ", ans1)
print("a ot in b = ", ans2)
print(" b in a = ",ans3)
print("b not in a = ",ans4)

c = [ 1, 2,3,[2,3]]
d = [ 2, 3]
print(c in d) #false
print( c not in d) # true
print(d in c) #true
print( d not in c) # false

dict1 = { 'k1' : 1 , 'k2' :2 ,'k3' :3 }
dict2 = {'k1' : 1 , 'k2' :2}
print(dict1 )
print(dict2 )


e = ( 2,3,4)
f = ( (2,3,4), 5,6,7)
print( e in  f)
print ( e not in f)
print ( f in e )
print( f not in e)




