import bip39_utils
import os

def main():
    # Load the BIP-39 word list
    word_list = bip39_utils.load_word_list()

    # Check if the mnemonic file exists, if not, create a new mnemonic
    if not os.path.exists('24w.txt'):
        # Create a 24-word mnemonic
        entropy = bip39_utils.generate_entropy()
        mnemonic = bip39_utils.entropy_to_mnemonic(entropy, word_list)
        bip39_utils.save_mnemonic_to_file(mnemonic, '24w.txt')

    # Read the 24-word mnemonic
    words = bip39_utils.load_mnemonic_from_file('24w.txt')

    # Ensure we only have 24 words
    assert len(words) == 24, "The mnemonic should contain exactly 24 words."

    # Get positions of words in the BIP-39 word list
    positions = [word_list.index(word) for word in words]

    # Pack words into blocks and encode
    block_size = 6  # Adjusted to 4 to ensure the number of blocks is consistent with earlier examples
    encoded_numbers = []
    
    for i in range(0, len(positions), block_size):
        block_positions = positions[i:i + block_size]
        # Pad the block_positions with zeros if necessary
        while len(block_positions) < block_size:
            block_positions.append(0)
        unique_number = bip39_utils.positions_to_number(block_positions, base=2048)
        combined_number = bip39_utils.combine_number_with_sequence(unique_number, i // block_size + 1)
        encoded_number = bip39_utils.encode_number(combined_number)
        encoded_numbers.append(encoded_number)
        print(f"Block: {block_positions} -> Unique Number: {unique_number} -> Combined Number: {combined_number} -> Encoded Number: {encoded_number}")

    # Save encoded numbers to file
    with open('24wp.txt', 'w') as file:
        for encoded_number in encoded_numbers:
            file.write(encoded_number + '\n')

    print("Packed numbers saved to 24wp.txt")

if __name__ == "__main__":
    main()
