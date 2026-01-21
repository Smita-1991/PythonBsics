###Inheritance
from Functions import Calculator

###This is child class
class ChildClass(Calculator):
    num2=100

    def __init__(self,num1,num2):
        self.BigNum=num1
        self.smallNum=num2

    def getCompleteData(self):
        return self.num2+self.num     ####num is the variable from the parent class

    def subtraction(self):
        return self.BigNum-self.smallNum

obj=ChildClass(50,20)
print(obj.getCompleteData())
print(obj.subtraction())

