import string

def load_bip39_wordlist(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def load_recovery_words(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split()[1] for line in file if line.strip()]

def generate_unique_number(positions, block_size):
    unique_number = 0
    for i, pos in enumerate(positions):
        unique_number += pos * (2048**(block_size - 1 - i))
    return unique_number

def decode_unique_number(unique_number, block_size):
    positions = []
    for i in range(block_size):
        pos = (unique_number // (2048**(block_size - 1 - i))) % 2048
        positions.append(pos)
    return positions

def base_convert(number, to_base=36):
    digits = string.digits + string.ascii_lowercase
    if number == 0:
        return digits[0]
    result = []
    while number:
        result.append(digits[number % to_base])
        number //= to_base
    return ''.join(reversed(result))

def base_convert_back(number_str, from_base=36):
    digits = string.digits + string.ascii_lowercase
    number = 0
    for char in number_str:
        number = number * from_base + digits.index(char)
    return number

def combine_sequence_and_number(sequence, unique_number, shift_amount):
    combined_number = (sequence << shift_amount) + unique_number
    return combined_number

def extract_sequence_and_number(combined_number, shift_amount):
    sequence = combined_number >> shift_amount
    unique_number = combined_number & ((1 << shift_amount) - 1)
    return sequence, unique_number

def save_packed_numbers(file_path, packed_numbers):
    with open(file_path, 'w') as file:
        for number in packed_numbers:
            file.write(f"{number}\n")

def load_packed_numbers(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]
