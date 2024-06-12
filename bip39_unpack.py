import bip39_utils

def main():
    # Load the BIP-39 word list
    word_list = bip39_utils.load_word_list()
    reverse_word_list = {index: word for index, word in enumerate(word_list)}

    # Read the packed numbers
    with open('24wp.txt', 'r') as file:
        encoded_numbers = [line.strip() for line in file.readlines() if line.strip()]

    # Decode each block
    decoded_blocks = []
    for encoded_number in encoded_numbers:
        combined_number = bip39_utils.decode_number(encoded_number)
        sequence, unique_number = bip39_utils.extract_sequence_from_combined_number(combined_number)
        positions = bip39_utils.number_to_positions(unique_number, base=2048, length=4)
        block = [reverse_word_list[pos] for pos in positions if pos in reverse_word_list]
        decoded_blocks.append((sequence, block))
        print(f"Encoded Number: {encoded_number} -> Combined Number: {combined_number} -> Sequence: {sequence} -> Unique Number: {unique_number} -> Positions: {positions} -> Block: {block}")

    # Sort blocks by sequence
    decoded_blocks.sort(key=lambda x: x[0])

    # Combine the blocks into a single word list
    decoded_words = [word for _, block in decoded_blocks for word in block if word != 'unknown']
    decoded_mnemonic = " ".join(decoded_words)

    print("\nDecoded 24-word mnemonic:")
    print(decoded_mnemonic)

    # Load the original mnemonic from the file for comparison
    original_words = bip39_utils.load_mnemonic_from_file('24w.txt')
    original_mnemonic = " ".join(original_words)

    print("\nOriginal 24-word mnemonic from 24w.txt:")
    print(original_mnemonic)

    # Check if the decoded mnemonic matches the original mnemonic
    if decoded_mnemonic == original_mnemonic:
        print("\nSuccess: The decoded mnemonic matches the original mnemonic.")
    else:
        print("\nError: The decoded mnemonic does not match the original mnemonic.")

if __name__ == "__main__":
    main()
