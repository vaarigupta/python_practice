class car :
    totalcar = 0
    def __init__(self,brand,year):
        # this is a constructor and it is also called
        #initialisation method and it is called whenever an object is created
        #always use self as its first parameter(which is a reference to the instance(object)
        #of the class)within the parenthesis and then arguments
        #always do assignment i.e. -> self.parameter = parameter
        #in order to referencing the parameter using self
        
        self.brand = brand
        self.year = year
        car.totalcar+=1
        print("AN INSTANCE IS CREATED")
       # print("total no of car",car.totalcar)

    def display(self):
        print("brand : ", self.brand)
        print("year : ", self.year)
    def __del__(self):
        car.totalcar-=2
    
car1 = car("bmw",2014)# object is created -> object_name = class(arguments)
car1.display() #accessing the members of the class -> object_name.member_name()

car2 = car("audi",2011)
car2.display()
car3 = car("maruti",2013)
car3.display()
car4 = car("ferrari",1990)
car4.display()
del car4
print(car.totalcar)
