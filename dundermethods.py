class Rat:

    def __init__(self,name):
        self.name = name
            
    def __setattr__(self, name, value):
        print(f'{name} set to {value}')
        self.__dict__[name] = value
    
    

rat = Rat('Mike')

print(rat.__dict__)

for i in rat.__dict__:
    print(rat.__dict__[i])

nums = [1,2,3,4,5,6,7,8,9]
b = map(lambda x : x + x ** x, nums)
print(list(b))

def filterxnums(x):
    return True if x < 3 else False

xnums = filter(lambda x: x < 3  ,nums)
znums = filter(filterxnums,nums)
print(list(xnums),list(znums))