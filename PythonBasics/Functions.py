
####Function declaration
def Greetme(name):
    print("Good Morning "+name)

####fuctioncall
Greetme("Smita")

#####Ooops demo
#Self keyword is mandatory for calling variables in method
#constructor name should be __init__
#new keyword is not required to create object


class Calculator:
    num=100   ####Class variable

    ##################Default constructor#########################
    def __init__(self,a,b):
        self.a=a        ####a and b are the instance variable and can be change on every object creation
        self.b=b

    def getData(self):
        print("Inside the method")

    def addition(self):
        return self.a+self.b+Calculator.num
        ### OR self.a+self.b+self.num
    def multiplication(self):
        return self.a*self.b


obj=Calculator(4,5)
obj.getData()
obj1=Calculator(10,20)
print(obj.addition())
print(obj1.multiplication())
print(obj.num)