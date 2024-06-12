# bip39 utils

Packing 24-wordlists into blocks, based on the bip39 english.txt wordlist.
in this example we create a wordlist, then pack it into 4 blocks
and extract them later back to the 24-wordlist.

How to use:

Source of the bip39 wordlist:
https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt

wget https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt


bip39_unique-wordlist.py
create 24w.txt

{
Mnemonic saved to 24w.txt:
isolate shield eagle music raise swim vital neither wolf mixed muffin empower room agree bomb alert twenty uncle click flee resist hill retire alone
}

bip39_check.py
checks if all words are in the bip39 word list and shows their position
{
24w.txt Position: 1, BIP-39 Number: 949
24w.txt Position: 2, BIP-39 Number: 1582
24w.txt Position: 3, BIP-39 Number: 553
...
24w.txt Position: 22, BIP-39 Number: 862
24w.txt Position: 23, BIP-39 Number: 1472
24w.txt Position: 24, BIP-39 Number: 56
}

bip39_pack.py
create 24wp.txt
{
Block: ['isolate', 'shield', 'eagle', 'music', 'raise', 'swim'] -> Positions: [949, 1582, 553, 1168, 1418, 1760] -> Unique Number: 34219163964454754016 -> Combined Number: 4756585646834099967712 -> Encoded Number: rvub2wsmvb8ov4
Block: ['vital', 'neither', 'wolf', 'mixed', 'muffin', 'empower'] -> Positions: [1961, 1186, 2023, 1138, 1162, 585] -> Unique Number: 70673352669050196553 -> Combined Number: 9515406318408340623945 -> Encoded Number: 1js5lgrqkttjbk9
Block: ['room', 'agree', 'bomb', 'alert', 'twenty', 'uncle'] -> Positions: [1504, 41, 202, 50, 1882, 1893] -> Unique Number: 54188033731529987941 -> Combined Number: 14221287482340465629029 -> Encoded Number: 2bdaob1fih215d1
Block: ['click', 'flee', 'resist', 'hill', 'retire', 'alone'] -> Positions: [342, 711, 1468, 862, 1472, 56] -> Unique Number: 12334369238405742648 -> Combined Number: 18901800300716986597432 -> Encoded Number: 32t30mf55z846yg
Packed numbers saved to 24wp.txt
}
cat 24wp.txt

rvub2wsmvb8ov4
1js5lgrqkttjbk9
2bdaob1fih215d1
32t30mf55z846yg

the order of the 4 blocks can be mixed(they have the order coded in the block)


bip39_unpack.py
displays wordlist
{
Encoded Number: rvub2wsmvb8ov4 -> Combined Number: 4756585646834099967712 -> Sequence: 1 -> Unique Number: 34219163964454754016 -> Positions: [949, 1582, 553, 1168, 1418, 1760] -> Block: ['isolate', 'shield', 'eagle', 'music', 'raise', 'swim']
Encoded Number: 1js5lgrqkttjbk9 -> Combined Number: 9515406318408340623945 -> Sequence: 2 -> Unique Number: 70673352669050196553 -> Positions: [1961, 1186, 2023, 1138, 1162, 585] -> Block: ['vital', 'neither', 'wolf', 'mixed', 'muffin', 'empower']
Encoded Number: 2bdaob1fih215d1 -> Combined Number: 14221287482340465629029 -> Sequence: 3 -> Unique Number: 54188033731529987941 -> Positions: [1504, 41, 202, 50, 1882, 1893] -> Block: ['room', 'agree', 'bomb', 'alert', 'twenty', 'uncle']
Encoded Number: 32t30mf55z846yg -> Combined Number: 18901800300716986597432 -> Sequence: 4 -> Unique Number: 12334369238405742648 -> Positions: [342, 711, 1468, 862, 1472, 56] -> Block: ['click', 'flee', 'resist', 'hill', 'retire', 'alone']
Sequence: 1 -> Block: ['isolate', 'shield', 'eagle', 'music', 'raise', 'swim']
Sequence: 2 -> Block: ['vital', 'neither', 'wolf', 'mixed', 'muffin', 'empower']
Sequence: 3 -> Block: ['room', 'agree', 'bomb', 'alert', 'twenty', 'uncle']
Sequence: 4 -> Block: ['click', 'flee', 'resist', 'hill', 'retire', 'alone']
}


use at your own risk!
higly experimental!
