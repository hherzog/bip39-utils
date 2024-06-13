from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64decode
import sys
import os
import bip39_utils

def derive_key(passphrase, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(passphrase.encode())

def decrypt(encrypted_data, passphrase):
    encrypted_data = urlsafe_b64decode(encrypted_data.encode())
    salt, iv, encrypted_data = encrypted_data[:16], encrypted_data[16:32], encrypted_data[32:]
    key = derive_key(passphrase, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    
    return data.decode()

def main(encrypted_data, passphrase):
    decrypted_data = decrypt(encrypted_data, passphrase)
    print("Decrypted data:", decrypted_data)

    # Write decrypted data to 24wp.txt
    with open('24wp.txt', 'w') as file:
        file.write(decrypted_data.replace(" ", "\n"))
    
    # Extract the wordlist
    encoded_numbers = decrypted_data.split()
    word_list = bip39_utils.load_word_list()
    reverse_word_list = {index: word for index, word in enumerate(word_list)}

    decoded_blocks = []
    for encoded_number in encoded_numbers:
        combined_number = bip39_utils.decode_number(encoded_number)
        sequence, unique_number = bip39_utils.extract_sequence_from_combined_number(combined_number)
        positions = bip39_utils.number_to_positions(unique_number, base=2048, length=4)
        block = [reverse_word_list[pos] for pos in positions if pos in reverse_word_list]
        decoded_blocks.append((sequence, block))

    decoded_blocks.sort(key=lambda x: x[0])
    decoded_words = [word for _, block in decoded_blocks for word in block if word != 'unknown']
    decoded_mnemonic = " ".join(decoded_words)

    print("\nDecoded 24-word mnemonic:")
    print(decoded_mnemonic)

    # Check if the original mnemonic file exists
    if os.path.exists('24w.txt'):
        original_words = bip39_utils.load_mnemonic_from_file('24w.txt')
        original_mnemonic = " ".join(original_words)

        print("\nOriginal 24-word mnemonic from 24w.txt:")
        print(original_mnemonic)

        # Check if the decoded mnemonic matches the original mnemonic
        if decoded_mnemonic == original_mnemonic:
            print("\nSuccess: The decoded mnemonic matches the original mnemonic.")
        else:
            print("\nError: The decoded mnemonic does not match the original mnemonic.")
    else:
        print("\nNo original mnemonic file (24w.txt) found. Skipping comparison.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <encrypted_data> <passphrase>")
        sys.exit(1)

    encrypted_data = sys.argv[1]
    passphrase = sys.argv[2]
    main(encrypted_data, passphrase)
