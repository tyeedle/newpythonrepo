
import json
dict1 = {}


values = [x for x in "aeiou aeiou"]
for i in range(len(values)):
    dict1[values[i]] =  values.count(values[i])

print(json.dumps(dict1,indent=4))

