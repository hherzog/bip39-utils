import os
import hashlib

# Load the BIP-39 word list
def load_word_list():
    with open('english.txt', 'r') as file:
        return [word.strip() for word in file.readlines()]

# Generate 256-bit entropy
def generate_entropy(bits=256):
    return os.urandom(bits // 8)

# Convert entropy to mnemonic phrase
def entropy_to_mnemonic(entropy, word_list):
    entropy_bits = bin(int.from_bytes(entropy, byteorder='big'))[2:].zfill(len(entropy) * 8)
    checksum_bits = bin(int(hashlib.sha256(entropy).hexdigest(), 16))[2:].zfill(256)[:len(entropy) * 8 // 32]
    bits = entropy_bits + checksum_bits
    chunks = [bits[i:i + 11] for i in range(0, len(bits), 11)]
    mnemonic = [word_list[int(chunk, 2)] for chunk in chunks]
    return ' '.join(mnemonic)

# Save mnemonic to file
def save_mnemonic_to_file(mnemonic, file_path='24w.txt'):
    with open(file_path, 'w') as file:
        file.write('\n'.join([f"{i+1} {word}" for i, word in enumerate(mnemonic.split())]))

def main():
    word_list = load_word_list()
    entropy = generate_entropy()
    mnemonic = entropy_to_mnemonic(entropy, word_list)
    save_mnemonic_to_file(mnemonic)
    print(f"Mnemonic saved to 24w.txt:\n{mnemonic}")

if __name__ == "__main__":
    main()
