# Importa as primitivas de cifragem, algoritmos e modos da biblioteca cryptography
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Importa o backend padrão para operações criptográficas
from cryptography.hazmat.backends import default_backend

# Importa as funções de padding, que adicionam bytes extras para alinhar os dados
from cryptography.hazmat.primitives import padding

# Importa o algoritmo PBKDF2HMAC para derivação de chave baseada em senha
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Importa algoritmos de hash para operações criptográficas
from cryptography.hazmat.primitives import hashes

# Importa o algoritmo Scrypt para derivação de chave segura
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

# Reimporta PBKDF2HMAC, usado para derivação de chaves baseada em senha (já importado anteriormente)
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Importa funções para serialização de chaves criptográficas
from cryptography.hazmat.primitives import serialization

# Importa o módulo os, usado para operações de sistema, como geração de bytes aleatórios
import os

# Função para gerar uma chave segura usando PBKDF2
def generate_key(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password)

# Função para criptografar o texto
def encrypt(data: bytes, key: bytes) -> bytes:
    iv = os.urandom(16)  # Vetor de inicialização (IV) aleatório de 16 bytes
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Adiciona padding para tornar o dado múltiplo do bloco AES (16 bytes)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext  # Retorna o IV + texto cifrado

# Função para descriptografar o texto
def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    iv = ciphertext[:16]  # Extraindo o IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    padded_data = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    
    # Remove o padding após a descriptografia
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

# Exemplo de uso
if __name__ == "__main__":
    password = b"senha-muito-segura"  # Deve ser uma senha forte
    salt = os.urandom(16)  # Sal aleatório
    key = generate_key(password, salt)
    
   # Texto original convertido para bytes usando encode
    texto_original = "Este é um texto secreto que será criptografado. ESPERO QUE VOCE ESTEJA BEM!".encode('utf-8')

    texto_criptografado = encrypt(texto_original, key)
    print(f"Texto criptografado: {texto_criptografado}")

    # Descriptografia
    texto_descriptografado = decrypt(texto_criptografado, key)
    print(f"Texto descriptografado: {texto_descriptografado.decode('utf-8')}")


