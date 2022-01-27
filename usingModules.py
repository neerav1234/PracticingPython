import pandas
from cryptography.fernet import Fernet

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"hey, This is the encypted flag.")
print(token)
print(f.decrypt(token))