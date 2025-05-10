import os 
import pyaes

key = b'elielgataozin123'

counter = pyaes.Counter(initial_value=1)


## Abrir o arquivo criptografado.
file_name = 'teste.txt'
file = open (file_name, 'rb')
file_data = file.read()
file.close()

### Chave de descriptografia 

aes = pyaes.AESModeOfOperationCTR(key, counter=counter)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

### criar um novo arquivo descriptografado 

new_file = 'test.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()