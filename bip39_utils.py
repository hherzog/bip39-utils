import os
import hashlib

def load_word_list(file_path='english.txt'):
    with open(file_path, 'r') as file:
        return [word.strip() for word in file.readlines()]

def create_mnemonic(word_list, words_count=24):
    entropy = os.urandom(words_count * 11 // 8)
    entropy_bits = bin(int.from_bytes(entropy, byteorder='big'))[2:].zfill(len(entropy) * 8)
    checksum_bits = bin(int(hashlib.sha256(entropy).hexdigest(), 16))[2:].zfill(256)[:words_count * 11 // 32]
    bits = entropy_bits + checksum_bits
    chunks = [bits[i:i + 11] for i in range(0, len(bits), 11)]
    mnemonic = [word_list[int(chunk, 2)] for chunk in chunks]
    return ' '.join(mnemonic)

def save_mnemonic_to_file(mnemonic, file_path='24w.txt'):
    with open(file_path, 'w') as file:
        file.write('\n'.join([f"{i+1} {word}" for i, word in enumerate(mnemonic.split())]))

def load_mnemonic_from_file(file_path='24w.txt'):
    with open(file_path, 'r') as file:
        return [line.strip().split()[1] for line in file.readlines() if line.strip()]

def generate_entropy(bits=256):
    return os.urandom(bits // 8)

def entropy_to_mnemonic(entropy, word_list):
    entropy_bits = bin(int.from_bytes(entropy, byteorder='big'))[2:].zfill(len(entropy) * 8)
    checksum_bits = bin(int(hashlib.sha256(entropy).hexdigest(), 16))[2:].zfill(256)[:len(entropy) * 8 // 32]
    bits = entropy_bits + checksum_bits
    chunks = [bits[i:i + 11] for i in range(0, len(bits), 11)]
    mnemonic = [word_list[int(chunk, 2)] for chunk in chunks]
    return ' '.join(mnemonic)

def positions_to_number(positions, base=2048):
    number = 0
    for pos in positions:
        number = number * base + pos
    return number

def number_to_positions(number, base=2048, length=4):
    positions = []
    while number:
        positions.append(number % base)
        number //= base
    while len(positions) < length:
        positions.append(0)
    positions.reverse()
    return positions

def combine_number_with_sequence(unique_number, sequence):
    return unique_number * 100 + sequence

def extract_sequence_from_combined_number(combined_number):
    sequence = combined_number % 100
    unique_number = combined_number // 100
    return sequence, unique_number

def encode_number(number):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    encoded = ""
    while number:
        number, remainder = divmod(number, 36)
        encoded = chars[remainder] + encoded
    return encoded

def decode_number(encoded):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    number = 0
    for char in encoded:
        number = number * 36 + chars.index(char)
    return number
