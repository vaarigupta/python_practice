n = int(input())
arr =  list(map (int , input().strip().split()))
arr = arr[:n+1]
print(arr)
##m1 = -1
##i=0
m1 = max(arr)
####while (i<n):
####    if(arr[i]>m1) :
####        m1 = arr[i]  
####    i+=1    
####print(m1)     
##print(m1)
##print(arr)
arr = arr.sort()
arr.reverse()
while (i<n):
    if(arr[i]<m1):
        print(m1)
        break
    i+=1
