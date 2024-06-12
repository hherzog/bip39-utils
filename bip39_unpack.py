from bip39_utils import load_bip39_wordlist, decode_unique_number, base_convert_back, extract_sequence_and_number, load_packed_numbers

def main():
    bip39_wordlist_path = 'english.txt'
    packed_numbers_path = '24wp.txt'
    block_size = 6  # Change this to 1, 2, 4, 6, or 8 as needed
    shift_amount = 72  # Must match the shift amount used in packing

    bip39_wordlist = load_bip39_wordlist(bip39_wordlist_path)
    packed_numbers = load_packed_numbers(packed_numbers_path)
    
    reverse_bip39_dict = {index + 1: word for index, word in enumerate(bip39_wordlist)}
    
    decoded_blocks = []
    for encoded_number in packed_numbers:
        combined_number = base_convert_back(encoded_number)
        sequence, unique_number = extract_sequence_and_number(combined_number, shift_amount)
        decoded_positions = decode_unique_number(unique_number, block_size)
        decoded_words = [reverse_bip39_dict.get(pos, "unknown") for pos in decoded_positions]
        decoded_blocks.append((sequence, decoded_words))
        print(f"Encoded Number: {encoded_number} -> Combined Number: {combined_number} -> Sequence: {sequence} -> Unique Number: {unique_number} -> Positions: {decoded_positions} -> Block: {decoded_words}")

    # Sort the blocks based on the sequence number
    decoded_blocks.sort(key=lambda x: x[0])
    
    for sequence, words in decoded_blocks:
        print(f"Sequence: {sequence} -> Block: {words}")

if __name__ == "__main__":
    main()
