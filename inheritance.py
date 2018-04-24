class car:
    string = "AN INSTANCE IS CREATED"
    def __init__(self):
        #self.brand = brand
        print("hello")

    def display(self):
        print("BRAND - BMW ")
        
# class subclas_name(superclass_name):

class mycar(car):
    car1 = "bmw"
    def __init__(self):
        print("SUBCLASS IS CREATED FROM SUPERCLASS")


# object_name = class_name(arguments)
carA = mycar() # instance is created of subclass 
print(carA.string)
carA.display()

