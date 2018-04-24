list1 = [1 ,2,3,4,5]
for num in list1 :
    if num ==2:
        break
        
       
    print(num)

print("......................")
start = 0
end = 10
step = 1
for num1 in range(start, end+1,3):
    if num1 == 3:
       continue
    print(num1)
print("......................")

for num3 in list1:
    for num1 in "abc":
        print(num3, num1)
print("......................")
        

i =0
while i<=5 :
    if(i==3):
        break
    print(i)
    i+=1

print("......................")
i = 4
while True :
    if(i==10):
        break
    print(i)
    i+=1


print("......................")

while True :
    pw = input("enter the password")
    if(pw == "vaari"): break
    print("access is denied")



print("......................")

start = 0
stop =True
step = 1

for num5 in range(start,stop,1):
    a = input("enter the correct no")
    if(a ==5):
        break
    print("found!")
    
    


    
    
    



    
    
