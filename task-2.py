a = "pyThOnn"
##print(len(a))
##print(type(a))
vl = ['a' , 'e' , 'i' , 'u' , 'o']
a = a.lower()
print(a)
count = 0
for i in a:
    if i in vl:
        count = count +1

print(count)
