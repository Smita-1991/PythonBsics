###Inheritance
### Import the parent class from the file in which the class is created  ### From Functions import Calculator
###While crating the child class send parent class name as an argument
###Create the default constructor and call the parent constructor by passing the arguments

from Functions import Calculator

###This is child class
class ChildClass(Calculator):
    num2=100

    def __init__(self):
        Calculator.__init__(self,2,3)

    def getCompleteData(self):
        return self.num2+self.num+self.addition()    ####num is the variable from the parent class

obj=ChildClass()
print("#### {}".format(obj.getCompleteData()))


