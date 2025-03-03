# Set and Get Private Object 
class member:
    def __init__(self,name):
        self.__name = name
        print(self.__name)
    def Set_Name(self,New_Name):
         self.__name = New_Name
    def Get_Name(self):
        return self.__name
one = member("Ahmed")
one.Set_Name("Osama")
print(one.Get_Name())
    
