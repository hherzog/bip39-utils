import bip39_utils
import sys
import time

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

def test_pack_unpack(iterations):
    word_list = bip39_utils.load_word_list()
    block_size = 4

    for i in range(1, iterations + 1):
        entropy = bip39_utils.generate_entropy()
        mnemonic = bip39_utils.entropy_to_mnemonic(entropy, word_list)
        words = mnemonic.split()
        positions = [word_list.index(word) for word in words]
        encoded_numbers = []
        
        for j in range(0, len(positions), block_size):
            block_positions = positions[j:j + block_size]
            # Ensure padding with a specific value if necessary (e.g., using -1)
            while len(block_positions) < block_size:
                block_positions.append(-1)
            unique_number = bip39_utils.positions_to_number(block_positions, base=2048)
            combined_number = bip39_utils.combine_number_with_sequence(unique_number, j // block_size + 1)
            encoded_number = bip39_utils.encode_number(combined_number)
            encoded_numbers.append(encoded_number)

        decoded_blocks = []
        for encoded_number in encoded_numbers:
            combined_number = bip39_utils.decode_number(encoded_number)
            sequence, unique_number = bip39_utils.extract_sequence_from_combined_number(combined_number)
            positions = bip39_utils.number_to_positions(unique_number, base=2048, length=4)
            block = [word_list[pos] if pos >= 0 else '' for pos in positions]
            decoded_blocks.append((sequence, block))

        decoded_blocks.sort(key=lambda x: x[0])
        decoded_words = [word for _, block in decoded_blocks for word in block if word]

        if decoded_words != words:
            print("\nError: The decoded mnemonic does not match the original mnemonic.")
            print("Original mnemonic:", words)
            print("Decoded mnemonic:", decoded_words)
            print("Blocks:")
            for seq, block in decoded_blocks:
                print(f"Sequence: {seq}, Block: {block}")
            break
        
        print_progress_bar(i, iterations, prefix='Progress:', suffix='Complete', length=50)
        time.sleep(0.1)  # Sleep to visualize progress bar

    if decoded_words == words:
        print("\nSuccess: All tests passed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number_of_tests>")
        sys.exit(1)

    try:
        number_of_tests = int(sys.argv[1])
    except ValueError:
        print("The number of tests should be an integer.")
        sys.exit(1)

    test_pack_unpack(number_of_tests)
