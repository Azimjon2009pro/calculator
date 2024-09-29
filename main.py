class Calculator:
    def __init__(self,num1: int,num2: int):
        self.num1: int = num1
        self.num2: int = num2
    def add(self):
        return self.num1 + self.num2
    
    def minus(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2
    
calc = Calculator(10,5)
print(calc.add())
print(calc.minus())
print(calc.multiply())
print(calc.divide())