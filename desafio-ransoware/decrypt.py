import os 
import pyaes

key = b'elielgataozin123'

counter = pyaes.Counter(initial_value=1)

file_name = 'teste.txt'

file = open (file_name, 'rb')
file_data = file.read()
file.close()


aes = pyaes.AESModeOfOperationCTR(key, counter=counter)
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()

print("[+] Arquivo descriptografado com sucesso!")
