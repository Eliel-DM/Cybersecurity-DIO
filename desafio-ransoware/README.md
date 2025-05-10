
# Criptografia AES com Modo CTR

Este projeto implementa a criptografia e descriptografia de arquivos usando o algoritmo AES (Advanced Encryption Standard) no modo **CTR (Counter Mode)**. O **pyaes** é utilizado para realizar a cifra e o modo de operação CTR, que utiliza um contador para gerar um fluxo de chave único.

## Funcionalidades

- **Criptografar** arquivos de texto usando uma chave de 16 bytes.
- **Descriptografar** arquivos criptografados usando a mesma chave e contador.
- O **modo CTR** permite criptografar e descriptografar dados de forma eficiente e segura.

## Requisitos

- Python 3.x
- Biblioteca `pyaes` (instalar via pip)

### Instalação das dependências

Para instalar as dependências necessárias para o projeto, execute:

```bash
pip install pyaes
```

## Estrutura do Projeto

O projeto possui os seguintes arquivos principais:

- `encrypt.py`: Script para criptografar um arquivo usando AES em modo CTR.
- `decrypt.py`: Script para descriptografar um arquivo previamente criptografado com AES em modo CTR.

## Como Usar

### 1. Criptografar um Arquivo

Para criptografar um arquivo de texto, execute o script `encrypt.py`. Ele irá abrir o arquivo, criptografá-lo e sobrescrever o arquivo com os dados criptografados.

#### Exemplo de uso:
```bash
python encrypt.py
```

O script pedirá para você informar o nome do arquivo e fará a criptografia. O arquivo criptografado será salvo com o mesmo nome.

### 2. Descriptografar um Arquivo

Para descriptografar um arquivo previamente criptografado, execute o script `decrypt.py`. Este script irá restaurar o arquivo original, desde que você forneça a chave correta usada na criptografia.

#### Exemplo de uso:
```bash
python decrypt.py
```

### 3. Chave e Contador

A chave utilizada para criptografar e descriptografar o arquivo deve ser de **16 bytes** (por exemplo, `b'elielgataozin123'`). O contador **`initial_value`** começa com **1** e é incrementado durante o processo de criptografia e descriptografia.

#### Exemplo de chave:
```python
key = b'elielgataozin123'  # Chave de 16 bytes
```

## Scripts

### `encrypt.py` – Criptografar um Arquivo

```python
import os
import pyaes

# Definindo a chave de 16 bytes
key = b'elielgataozin123'

# Contador fixo
counter = pyaes.Counter(initial_value=1)

# Abrir arquivo para criptografar
with open('teste.txt', 'rb') as file:
    file_data = file.read()

# Criptografando os dados
aes = pyaes.AESModeOfOperationCTR(key, counter=counter)
encrypted_data = aes.encrypt(file_data)

# Salvar os dados criptografados
with open('teste_criptografado.txt', 'wb') as file:
    file.write(encrypted_data)

print("[+] Arquivo criptografado com sucesso!")
```

### `decrypt.py` – Descriptografar um Arquivo

```python
import os
import pyaes

# Arquivo criptografado
file_name = 'teste_criptografado.txt'

# Abrir arquivo criptografado
with open(file_name, 'rb') as file:
    file_data = file.read()

# Chave de 16 bytes
key = b'elielgataozin123'

# Mesmo contador usado na criptografia
counter = pyaes.Counter(initial_value=1)

# Descriptografar
aes = pyaes.AESModeOfOperationCTR(key, counter=counter)
decrypt_data = aes.decrypt(file_data)

# Remover arquivo criptografado
os.remove(file_name)

# Salvar arquivo descriptografado
with open('teste_descriptografado.txt', 'wb') as file:
    file.write(decrypt_data)

print("[+] Arquivo descriptografado com sucesso!")
```

## Considerações

- **Segurança**: Ao utilizar o modo **CTR**, o contador nunca deve se repetir para garantir a segurança. Este projeto usa um contador fixo para fins de demonstração. Em um sistema real, o contador deve ser aleatório e único por criptografia.
- **Desempenho**: O modo **CTR** permite a criptografia e descriptografia em paralelo, proporcionando melhor desempenho em ambientes com múltiplos núcleos de CPU.
- **Chave**: A chave deve ser mantida em segredo e usada corretamente na criptografia e na descriptografia.

## Contribuições

Contribuições são bem-vindas! Se você tiver melhorias, correções ou sugestões, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.
