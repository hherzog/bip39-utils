import bip39_utils
import bip39_utils_crypt
import bip39_utils_qrcode
import os
import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        print_help()
        return
    
    passphrase = sys.argv[1] if len(sys.argv) > 1 else None
    mode = sys.argv[2] if len(sys.argv) > 2 else None
    generate_qr = sys.argv[3] == "QR" if len(sys.argv) > 3 else False

    if passphrase and not mode:
        print_help()
        return

    word_list = bip39_utils.load_word_list()

    if not os.path.exists('24w.txt'):
        entropy = bip39_utils.generate_entropy()
        mnemonic = bip39_utils.entropy_to_mnemonic(entropy, word_list)
        bip39_utils.save_mnemonic_to_file(mnemonic, '24w.txt')

    words = bip39_utils.load_mnemonic_from_file('24w.txt')
    assert len(words) == 24, "The mnemonic should contain exactly 24 words."

    positions = [word_list.index(word) for word in words]

    block_size = 6
    encoded_numbers = []
    for i in range(0, len(positions), block_size):
        block_positions = positions[i:i + block_size]
        while len(block_positions) < block_size:
            block_positions.append(0)
        unique_number = bip39_utils.positions_to_number(block_positions, base=2048)
        combined_number = bip39_utils.combine_number_with_sequence(unique_number, i // block_size + 1)
        encoded_number = bip39_utils.encode_number(combined_number)
        encoded_numbers.append(encoded_number)
        print(f"Block: {block_positions} -> Unique Number: {unique_number} -> Combined Number: {combined_number} -> Encoded Number: {encoded_number}")

    packed_data = '\n'.join(encoded_numbers)
    
    # Save plain blocks to 24wp.txt
    with open('24wp.txt', 'w') as file:
        file.write(packed_data)
    
    if passphrase and mode:
        encrypted_blocks = [bip39_utils_crypt.encrypt(block, passphrase, mode) for block in encoded_numbers]
        combined_encrypted_data = bip39_utils_crypt.encrypt(packed_data, passphrase, mode)
        
        print("\nEncrypted Blocks:")
        for i, encrypted_block in enumerate(encrypted_blocks):
            print(f"Encrypted block {i + 1}: {encrypted_block}")
            if generate_qr:
                bip39_utils_qrcode.create_qr_code(encrypted_block, f"block_{i + 1}_qr.png")
                print(f"QR code for block {i + 1} generated as block_{i + 1}_qr.png")
        
        print("\nCombined Encrypted Block:")
        print(combined_encrypted_data)
        if generate_qr:
            bip39_utils_qrcode.create_qr_code(combined_encrypted_data, "combined_qr.png")
            print("Combined QR code generated as combined_qr.png")
    else:
        print("Packed numbers saved to 24wp.txt")

def print_help():
    print("Usage: python3 bip39_pack.py [passphrase] [mode] [QR]")
    print("If no passphrase and mode are provided, the data will be saved without encryption.")
    print("Modes: GCM, CFB")
    print("Optional 'QR' parameter to generate QR codes for encrypted blocks and combined encrypted block.")

if __name__ == "__main__":
    main()
