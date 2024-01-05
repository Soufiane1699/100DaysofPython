from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

with open('schlüssel.txt', 'wb') as write_key:
    write_key.write(key)

f = Fernet(key)
token = f.encrypt(b'My Deep Secret.')
print(token)

token = f.decrypt(token)
print(token)

