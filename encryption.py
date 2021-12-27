from cryptography.fernet import Fernet

s = "123"

key = Fernet.generate_key()

fernet = Fernet(key)

encodedString = fernet.encrypt(s.encode())

print(f"regular string : {s}, encrypted : {encodedString}")

print(f"decrypted : {fernet.decrypt(encodedString), }")

a = ["Hello This Is Password 1","Hello This Is Password 2"]

for i,v in enumerate(a):
    k = fernet.generate_key()
    fernetE = Fernet(k)
    encoded = fernet.encrypt(v.encode())
    print(f'encrypted : {encoded}')
    print(f'decrypted : {fernet.decrypt(encoded)}')