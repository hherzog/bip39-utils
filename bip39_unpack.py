import bip39_utils
import bip39_utils_crypt
import sys
import os
from cryptography.exceptions import InvalidTag

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        print_help()
        return

    passphrase = sys.argv[1] if len(sys.argv) > 1 else None
    encrypted_data = sys.argv[2] if len(sys.argv) > 2 else None

    if passphrase and not encrypted_data:
        print_help()
        return

    word_list = bip39_utils.load_word_list()
    reverse_word_list = {index: word for index, word in enumerate(word_list)}

    if passphrase and encrypted_data:
        try:
            packed_data = bip39_utils_crypt.decrypt(encrypted_data, passphrase)
            print("Decrypted data:", packed_data)
        except (ValueError, InvalidTag) as e:
            print("Decryption failed. The passphrase might be incorrect.")
            return
    else:
        with open('24wp.txt', 'r') as file:
            packed_data = file.read().strip()

    encoded_numbers = packed_data.split()
    decoded_blocks = []
    for encoded_number in encoded_numbers:
        combined_number = bip39_utils.decode_number(encoded_number)
        sequence, unique_number = bip39_utils.extract_sequence_from_combined_number(combined_number)
        positions = bip39_utils.number_to_positions(unique_number, base=2048)
        block = [reverse_word_list[pos] for pos in positions if pos in reverse_word_list]
        decoded_blocks.append((sequence, block, positions))
        print(f"Encoded Number: {encoded_number} -> Combined Number: {combined_number} -> Sequence: {sequence} -> Unique Number: {unique_number} -> Positions: {positions} -> Block: {block}")

    if len(decoded_blocks) == 1:
        sequence, block, positions = decoded_blocks[0]
        numbered_block = [f"{(sequence-1)*len(block) + i + 1} {word}" for i, word in enumerate(block)]
        print("\nDecoded block corresponding to sequence number:")
        print(f"Sequence: {sequence}, Block: {numbered_block}, Positions: {positions}")

        # Check against 24w.txt if it exists
        if os.path.exists('24w.txt'):
            original_words = bip39_utils.load_mnemonic_from_file('24w.txt')
            original_block = original_words[(sequence-1)*len(block) : sequence*len(block)]
            
            if block == original_block:
                print("\nSuccess: The decoded block matches the original mnemonic block.")
            else:
                print("\nError: The decoded block does not match the original mnemonic block.")
                print("Original block:", original_block)
                print("Decoded block:", block)
    else:
        decoded_blocks.sort(key=lambda x: x[0])
        decoded_words = [word for _, block, _ in decoded_blocks for word in block if word != 'unknown']
        decoded_mnemonic = " ".join(decoded_words)

        print("\nDecoded 24-word mnemonic:")
        print(decoded_mnemonic)

        if os.path.exists('24w.txt'):
            original_words = bip39_utils.load_mnemonic_from_file('24w.txt')
            original_mnemonic = " ".join(original_words)

            print("\nOriginal 24-word mnemonic from 24w.txt:")
            print(original_mnemonic)

            if decoded_mnemonic == original_mnemonic:
                print("\nSuccess: The decoded mnemonic matches the original mnemonic.")
            else:
                print("\nError: The decoded mnemonic does not match the original mnemonic.")

def print_help():
    print("Usage: python3 bip39_unpack.py [passphrase] [encrypted_data]")
    print("If no passphrase and encrypted data are provided, the data will be read without decryption.")
    print("Modes: GCM, CFB")

if __name__ == "__main__":
    main()
