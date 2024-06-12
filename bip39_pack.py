from bip39_utils import load_bip39_wordlist, load_recovery_words, generate_unique_number, base_convert, combine_sequence_and_number, save_packed_numbers

def main():
    bip39_wordlist_path = 'english.txt'
    recovery_words_path = '24w.txt'
    packed_numbers_path = '24wp.txt'
    block_size = 6  # Change this to 1, 2, 4, 6, or 8 as needed
    shift_amount = 72  # Increased to accommodate larger values for block size 8

    bip39_wordlist = load_bip39_wordlist(bip39_wordlist_path)
    recovery_words = load_recovery_words(recovery_words_path)
    
    bip39_dict = {word: index + 1 for index, word in enumerate(bip39_wordlist)}
    
    # Verify that the number of recovery words is a multiple of block_size
    if len(recovery_words) % block_size != 0:
        print(f"Error: The recovery phrase must contain a multiple of {block_size} words.")
        return

    packed_numbers = []
    for i in range(0, len(recovery_words), block_size):
        block = recovery_words[i:i+block_size]
        positions = [bip39_dict[word] for word in block]
        unique_number = generate_unique_number(positions, block_size)
        combined_number = combine_sequence_and_number(i // block_size + 1, unique_number, shift_amount)
        encoded_number = base_convert(combined_number)
        packed_numbers.append(encoded_number)
        print(f"Block: {block} -> Positions: {positions} -> Unique Number: {unique_number} -> Combined Number: {combined_number} -> Encoded Number: {encoded_number}")
    
    save_packed_numbers(packed_numbers_path, packed_numbers)
    print(f"Packed numbers saved to {packed_numbers_path}")

if __name__ == "__main__":
    main()
