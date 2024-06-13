import bip39_utils

def main():
    # Load the BIP-39 word list
    word_list = bip39_utils.load_word_list()

    # Generate 256-bit entropy
    entropy = bip39_utils.generate_entropy()

    # Convert entropy to mnemonic phrase
    mnemonic = bip39_utils.entropy_to_mnemonic(entropy, word_list)

    # Save mnemonic to file
    bip39_utils.save_mnemonic_to_file(mnemonic)
    print(f"Mnemonic saved to 24w.txt:\n{mnemonic}")

if __name__ == "__main__":
    main()
