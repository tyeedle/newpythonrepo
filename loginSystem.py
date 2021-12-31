import json
import random
class User:
    
    def __init__(self):
        id = random.randint(1,10000)
        with open('acc.json','r') as f:
            self.accRead = json.load(f)

        
        mode = input('MODE : [LOG]IN - [REG]ISTER \n >>> ').upper()
        if mode == "REG":
            try: 
                username = input("username \n >>> ")
                password = input("password \n >>> ")

                self.accRead['Usernames'][id] = username
                self.accRead['Passwords'][id] = password

                print(f'ID generated, id={id} | user={username} | pass={password}')

                with open('acc.json','w') as f:
                    json.dump(self.accRead,f)
        
            except :
                print('Exception Error')
        if mode == "LOG":
            id_ = input("ENTER [ID] \n >>> ")
            
            for k,v in self.accRead['Usernames'].items():
                if id_ == k:
                    pasw = input("ENTER [PASSWORD] \n >>> ")
                    passForID = self.accRead['Passwords'][id_]
                    if pasw == passForID:
                        print('STATUS : <LOGGED IN>')
                    else:
                       print('incorrect password')
                
                elif id_ != k:
                    print('incorrect id')

            

    
user = User()