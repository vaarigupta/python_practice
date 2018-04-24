year = int(input())
def is_leap(y):
    if((y%4==0)and(y%400==0)):
        print("True")
    elif((y%100==0)and(y%2==0)):
        print("False")
        
        
        
is_leap(year)        
        
