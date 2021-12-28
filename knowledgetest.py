import json
import requests


def ff1(x):
    return True if x == 1 or x == 2 else False 



arr = [1,2,3]



arr2 = [x for x in arr if x == 2 or x == 1]

arr3 = filter(ff1,arr)

r = requests.get('https://api.github.com/user',auth=('user','pass'))

print(r.text)

data = json.dumps(r.text,indent=2)

load = json.loads(data)

with open('apidata.json','w') as jfile:
    json.dump(load, jfile)



