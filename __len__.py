class member:
    def __init__(self):
        self.skills = ["HTML","CPP","JAVA"]
    def __len__(self):
        return len(self.skills)
Man1=member()
print((Man1))
print(Man1.__len__())
print(len(Man1))
