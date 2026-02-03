class BasicCalculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Addition(self):
        return self.num1 + self.num2

    def Subtraction(self):
        return self.num1 - self.num2

    def Multiplication(self):
        return self.num1 * self.num2

    def Division(self):
        return self.num1 / self.num2



basicCalculator = BasicCalculator(10,5)

print("Addition:",basicCalculator.Addition())
print("Subtraction:",basicCalculator.Subtraction())
print("Multiplication",basicCalculator.Subtraction())
print("Division",basicCalculator.Division())
