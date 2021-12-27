from cryptography.fernet import Fernet

for i in range(50):
        k = Fernet.generate_key()
        fernet = Fernet(k)





