# method class 
class member:
    def __init__(self,First_Name,Last_Name,gender):
        self.f_name=First_Name
        self.l_name=Last_Name
        self.gender=gender
    def Get_FullName(self):
        return f"{self.f_name} {self.l_name}"
    def Say_Hello(self):
        if self.gender == "Male":
            return f"Hello Mr {self.f_name} {self.l_name}"
        elif self.gender == "female":
            return f"Hello Miss {self.f_name} {self.l_name}"
        else :
            return f"Hello {self.f_name} {self.l_name}"
member_one=member("Osama","Rayan","Male")   
member_Two=member("Mona","Ahmed","female")
member_Three=member("Mona","Ahmed","fa")
print(member_one.Get_FullName())
print(member_one.Say_Hello())
print(member_Two.Say_Hello())
print(member_Three.Say_Hello())

    
