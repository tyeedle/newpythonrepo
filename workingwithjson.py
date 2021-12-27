import json

data = {
    'client1' : {
        "name" : 'Mike Dickinson',
        'age' : '25',
        'occupation' : 'Docto'
    }   
}




with open('wwj.json','r') as jfile:
    dataDecoded = json.load(jfile)

dataDecoded['Names'].append("John")

for k,v in dataDecoded.items():
    
    dataDecoded[k].append({"age" : "1"})
    print(dataDecoded)