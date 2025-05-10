import os 
import pyaes

file_name = 'teste.txt'


file_name = 'teste.txt'
file = open (file_name, 'rb')
file_data = file.read()
file.close()

key = b'elielgataozin123'

counter = pyaes.Counter(initial_value=1)

aes = pyaes.AESModeOfOperationCTR(key, counter=counter)
crypto_data = aes.encrypt(file_data)

with open(file_name, 'wb') as file:
    file.write(crypto_data)

print("[+] Arquivo criptografado com sucesso!")

