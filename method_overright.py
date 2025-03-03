# Inheritance 
class Food:
    def __init__(self,Name):
        self.Name = Name
        print(f"{self.Name} is very Good For You it is help you")
    def eat(self):
        print("Hello Form Base Class")
class Apple(Food):
    def __init__(self,Name,Age):
        super().__init__(Name)
        self.Age=Age
        print(f"{self.Name} From Drived Class and His Age is {self.Age}")
    # method over right 
    def eat(self):
        print("Hello Form Drived Class")
Two = Apple("Samuel",22)
Two.eat()

    
