class Member:
    user_count = 0  # يجب أن يكون محاذياً بشكل صحيح
    @staticmethod
    def Say_Helloo():
        print("Hello Everyone ")
    @classmethod
    def show_users_count(cls):
        print(f"Users count: {cls.user_count}")

    def __init__(self, First_Name, Last_Name, gender):
        self.f_name = First_Name
        self.l_name = Last_Name
        self.gender = gender.capitalize()  # لضمان تطابق القيم دائمًا
        Member.user_count += 1

    def Get_FullName(self):
        return f"{self.f_name} {self.l_name}"

    def Say_Hello(self):
        if self.gender == "Male":
            return f"Hello Mr {self.f_name} {self.l_name}"
        elif self.gender == "Female":
            return f"Hello Miss {self.f_name} {self.l_name}"
        else:
            return f"Hello {self.f_name} {self.l_name}"

    def Delete_Clients(self):
        Member.user_count -= 1
        return Member.user_count 
# إنشاء الكائنات
member_one = Member("Osama", "Rayan", "Male")
member_two = Member("Mona", "Ahmed", "female")
member_three = Member("Mona", "Ahmed", "fa")  # قيمة غير صحيحة
Member.Say_Helloo()
print(member_one.Delete_Clients())
# طباعة النتائج
print(member_one.Get_FullName())
print(member_one.Say_Hello())
print(member_two.Say_Hello())
print(member_three.Say_Hello())

# عرض عدد المستخدمين
Member.show_users_count()
