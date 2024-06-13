import qrcode
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

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
        iv = os.urandom(12)  # GCM standard IV size is 12 bytes
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
        return urlsafe_b64encode(b'GCM:' + salt + iv + encryptor.tag + encrypted_data).decode()
    elif mode == 'CFB':
        iv = os.urandom(16)  # CFB standard IV size is 16 bytes
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
    salt = encrypted_data[:16]
    if mode_prefix == b'GCM:':
        iv, tag, encrypted_data = encrypted_data[16:28], encrypted_data[28:44], encrypted_data[44:]
        key = derive_key(passphrase, salt)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        data = decryptor.update(encrypted_data) + decryptor.finalize()
    elif mode_prefix == b'CFB:':
        iv, encrypted_data = encrypted_data[16:32], encrypted_data[32:]
        key = derive_key(passphrase, salt)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
    else:
        raise ValueError("Unsupported encryption mode")
    return data.decode()

def read_encoded_blocks(file_path='24wp.txt'):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

def main(passphrase, mode):
    # Read the encoded blocks from 24wp.txt
    encoded_blocks = read_encoded_blocks('24wp.txt')

    # Combine all blocks into one QR code
    combined_string = " ".join(encoded_blocks)
    encrypted_combined_string = encrypt(combined_string, passphrase, mode)
    generate_qr_code(encrypted_combined_string, "combined_qr.png")
    print("Combined QR code generated as combined_qr.png")
    print(f"Combined encrypted block: {encrypted_combined_string}")

    # Generate separate QR codes for each block
    for i, block in enumerate(encoded_blocks):
        encrypted_block = encrypt(block, passphrase, mode)
        generate_qr_code(encrypted_block, f"block_{i+1}_qr.png")
        print(f"QR code for block {i+1} generated as block_{i+1}_qr.png")
        print(f"Encrypted block {i+1}: {encrypted_block}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <passphrase> <mode (GCM/CFB)>")
        sys.exit(1)

    passphrase = sys.argv[1]
    mode = sys.argv[2]
    main(passphrase, mode)
