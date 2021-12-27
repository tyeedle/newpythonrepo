from cryptography.fernet import Fernet


k = Fernet.generate_key()
fernet = Fernet(k)

with open('filekey.key','wb') as filekey:
        filekey.write(k)



users = []
websites = []
passwords = []

def CreatePassword():
        user_id = 0

        
        

                
        while True:
                username = input('Enter Username : \n > ')

                useFor = input('Enter Website Or Whatever : \n > ')
                password = input('Enter Password : \n > ')
                users.append(username)
                websites.append(useFor)
                passwords.append(password)
                        
                
                edata = (f'> {users[user_id] , websites[user_id], passwords[user_id]}\n')
        

                
                        
                passwords_encrypted = fernet.encrypt(edata.encode())
                
                

                with open('passwordsStorage.txt','ab') as passw:
                        passw.write(f'{passwords_encrypted}\n'.encode() )                       
                        
                
                showpasses = input('show? \n > ')

                if showpasses == "y":
                        with open('passwordsStorage.txt','rb') as bytesfile:
                                readB = bytesfile.read()
                        
                
                        admin = input("enter as admin? [y/n] \n > ")
                        if admin == "y":
                                passwforadmin = input("Enter Admin Password. \n > ")
                                if passwforadmin == "adminT":
                                        print('printing as admin.')
                                        print(de)        
                                
                                

                        
                        else:
                                print('printing as normal user.')
                                print(readB) 
                else:
                        print('printing as normal user.')
                        print(readB)              

                user_id += 1
CreatePassword()