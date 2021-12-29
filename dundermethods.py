import json


class Person:
    objects_dict = {}
    objects_created = 0
    def __init__(self,name,age,incomePerAnum):
        Person.objects_created += 1

        self.name = name
        
        self.age = age
        self.incomePerAnum = incomePerAnum

        Person.objects_dict[self.name] = {"incomePerYear" : incomePerAnum , "age"  : age}

    

    def __eq__(self,other):
        return False
    
    def __repr__(self):
        return "Person Object"
    


p1 = Person("John", 24, 100000)
p2 = Person("Bob", 36, 120000)
p3 = Person("Alice",40,145000)


with open("dunderjsonfile.json",'w') as f:
    json.dump(Person.objects_dict,f)

def loaded():
    with open("dunderjsonfile.json",'r') as f:
        loaded = json.load(f)
    return loaded

print(json.dumps(Person.objects_dict,indent=4))