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
class Car:
    def __init__(self, name: str,motor: str,model: str,speed: int,money: int):
        self.name: str = name
        self.motor: str = motor
        self.model: str = model
        self.speed: int = speed
        self.money: int = money


class Bmw(Car):
    def __init__(self,name, motor, model, speed, money):
        super().__init__(name,motor, model, speed, money)

    def about_car(self):
        return f"The cars name is {self.name}, and it's motor: {self.motor}, the maximum speed of car is {self.speed},anf finally car costs{self.money}"
    
class Mercesed(Car):
    def __init__(self,name, motor, model, speed, money):
        super().__init__(name,motor, model, speed, money)

    def about_car(self):
        return f"The cars name is {self.name}, and it's motor: {self.motor}, the maximum speed of car is {self.speed},anf finally car costs{self.money}"
    
bmw = Bmw("Bmw","Motor_Bmw123","M5 f90",2500,10000)
print(bmw.about_car())
merc = Mercesed("Mercedec","Motor_Benz233","Cls",2000,303444)
print(merc.about_car())