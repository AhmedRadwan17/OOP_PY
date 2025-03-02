class member:
    def __init__(self):
        self.skills = ["HTML","CPP","JAVA"]
    def __str__(self):
        return f"My Skills are: {self.skills}"
Man1=member()
print(Man1)
Man1.skills.append("PHP")
print(Man1)

"""
--------------------------------------
    Without Using __str__ The Output Will Print => <__main__.member object at 0x7b44506a1400>
    When You Using __str__ The OutPut Will Print My Skills are: ['HTML', 'CPP', 'JAVA']
--------------------------------------
"""
