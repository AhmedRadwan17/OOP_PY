# multiple Inheritance 
class Food:
    def __init__(self):
        print("Base Class!")
    def eat(self):
        print("Hello")
class Apple(Food):
    def __init__(self):
        print("Drived Class")
class Inhert(Apple):
    pass
one=Inhert()
one.eat()


    
