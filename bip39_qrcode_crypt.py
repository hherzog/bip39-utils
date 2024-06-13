import qrcode
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
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

def encrypt(data, passphrase):
    salt = os.urandom(16)
    key = derive_key(passphrase, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return urlsafe_b64encode(salt + iv + encrypted_data).decode()

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

def main(passphrase):
    # Read the encoded blocks from 24wp.txt
    encoded_blocks = read_encoded_blocks('24wp.txt')

    # Option 1: Combine all blocks into one QR code
    combined_string = " ".join(encoded_blocks)
    encrypted_combined_string = encrypt(combined_string, passphrase)
    generate_qr_code(encrypted_combined_string, "combined_qr.png")
    print("Combined QR code generated as combined_qr.png")
    print(f"Combined encrypted block: {encrypted_combined_string}")

    # Option 2: Generate separate QR codes for each block
    for i, block in enumerate(encoded_blocks):
        encrypted_block = encrypt(block, passphrase)
        generate_qr_code(encrypted_block, f"block_{i+1}_qr.png")
        print(f"QR code for block {i+1} generated as block_{i+1}_qr.png")
        print(f"Encrypted block {i+1}: {encrypted_block}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <passphrase>")
        sys.exit(1)

    passphrase = sys.argv[1]
    main(passphrase)
