class Person:

    def __init__(self,fname,lname,age,incomePerAnum):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.incomePerAnum = incomePerAnum
    
    def __eq__(self,other):
        return "Same Family" if self.lname == other.lname else False
    
p1 = Person("John", "Davis", 24, 100000)
p2 = Person("Bob", "Davis", 36, 120000)

print(p1 == p2)

print(p2.__dict__['fname'])
