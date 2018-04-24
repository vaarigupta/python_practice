#without arguments

def pagal():
    print("hello bc")


pagal()    

print(".....................")


#with argument
def hello(name1="pgl"):
    print("hello",name1)


name = "raavi"
hello()
print(".....................")

#with return keyword
def sum(num1 , num2):
    ans = num1 + num2
    return ans



a = 100
b = 290
print(sum(a,b))

print(".....................")

#using lang defined identifier __doc__

def yashu(a,b):
    "heloo ap kse hai"
    "where do u live"
    ans = a//b
    return ans



print(yashu.__doc__)

print(".....................")
# anonymous function using lambda keyword


diff = lambda a, b , c : a - b *c

print(diff(3,5,6))









    
