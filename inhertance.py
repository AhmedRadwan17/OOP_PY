class Food:
    def __init__(self,name, Price):
        self.name=name
        self.Price=Price
        print(f"{self.name} is Created From Base Class and His Price is {self.Price}")
        
    def eat(self):
        print("Eat method From Base Class")
class Apple(Food):
    def __init__(self,name,Price):
        # Two Ways To inhert From Base Class:
       # (First Way) Food.__init__(self,name,price)
       # (Second Way)
       super().__init__(name,Price)
       
       print(f"{self.name}Is Created From Drived Class and Price is {self.Price}")

print("-" * 20)
one = Apple("Pizza",200)
Two = Food("Pizza",500)
print("-" * 20)
one.eat()
