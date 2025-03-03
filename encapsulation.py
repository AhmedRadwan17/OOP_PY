# Encapsulation 
"""
KeyWord => Protected _ (_name)
KeyWord => Privated __ (__name)
"""
class member:
    def __init__(self,name):
        # Protected
        self._name = name
one = member("Ahmed")

"""
    (Protected Allow To call it in any
    Class and Allow Outside Class But
    You Should Write Name Name Like
    This) => one = member() 
   ---------------------------------
    ---print(one._name) => Ahmed ---
    ---------------------------------
"""
class member:
    def __init__(self,name):
        # Private 
        self.__name = name
    def Print(self):
        print(self.__name)
    
one = member("Ahmed")
one.Print() # output => "Ahmed"
# print(one.__name) (error As Privated)
"""
    (Privated don't Allow To call it in
    any Class and it 's allow to call 
    in only class We can only access 
    From Inside Class like this 
      
      def Print(self):
          print(self.__name)
          
   ---------------------------------
    ---print(one.__name) => error ---
    ---------------------------------
"""
print(one._member__name)

"""
     You Can Print Private Object 
     There are lots of rules that you
     should Follow it 
     (1) Name of instance 
     (2) Write (_)
     (3) Name of Class
     (4) Write The Privated object
       ----- Like This -----
 --Print(one_member__name)-- 
                   =>(OutPut) Ahmed
"""
