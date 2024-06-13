import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode

def derive_key(passphrase, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(passphrase.encode())

def encrypt(data, passphrase, mode='GCM'):
    salt = os.urandom(16)
    key = derive_key(passphrase, salt)

    if mode == 'GCM':
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
        return urlsafe_b64encode(b'GCM:' + salt + iv + encryptor.tag + encrypted_data).decode()

    elif mode == 'CFB':
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return urlsafe_b64encode(b'CFB:' + salt + iv + encrypted_data).decode()
    
    else:
        raise ValueError("Unsupported encryption mode")

def decrypt(encrypted_data, passphrase):
    encrypted_data = urlsafe_b64decode(encrypted_data.encode())
    mode_prefix = encrypted_data[:4]
    encrypted_data = encrypted_data[4:]

    if mode_prefix == b'GCM:':
        salt, iv, tag, encrypted_data = encrypted_data[:16], encrypted_data[16:28], encrypted_data[28:44], encrypted_data[44:]
        key = derive_key(passphrase, salt)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        data = decryptor.update(encrypted_data) + decryptor.finalize()
        return data.decode()

    elif mode_prefix == b'CFB:':
        salt, iv, encrypted_data = encrypted_data[:16], encrypted_data[16:32], encrypted_data[32:]
        key = derive_key(passphrase, salt)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        return data.decode()

    else:
        raise ValueError("Unsupported encryption mode")
