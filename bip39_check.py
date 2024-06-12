def load_bip39_wordlist(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def load_recovery_words(file_path):
    with open(file_path, 'r') as file:
        return [(int(line.split()[0]), line.split()[1]) for line in file if line.strip()]

def check_recovery_words(bip39_wordlist, recovery_words):
    bip39_dict = {word: index + 1 for index, word in enumerate(bip39_wordlist)}
    recovery_numbers = [(position, bip39_dict[word]) for position, word in recovery_words if word in bip39_dict]
    return recovery_numbers

def main():
    bip39_wordlist_path = 'english.txt'
    recovery_words_path = '24w.txt'

    bip39_wordlist = load_bip39_wordlist(bip39_wordlist_path)
    recovery_words = load_recovery_words(recovery_words_path)
    recovery_numbers = check_recovery_words(bip39_wordlist, recovery_words)
    
    for position, bip39_number in recovery_numbers:
        print(f"24w.txt Position: {position}, BIP-39 Number: {bip39_number}")

if __name__ == "__main__":
    main()
