# bip39 utils</br>

Packing 24-wordlists into blocks, based on the bip39 english.txt wordlist.</br>
In this example we create a wordlist, then pack it into 4 blocks</br>
and extract them later back to the 24-wordlist.</br>

How to use:</br>

Source of the bip39 wordlist:</br>
https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt</br>
https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt</br>

wget https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt</br>


python3 bip39_unique-wordlist.py</br>
create 24w.txt</br>
{</br>
Mnemonic saved to 24w.txt:</br>
pet rate galaxy ring claw cereal quiz swing acoustic guilt argue retire cinnamon satoshi doll arrow subway guilt burden stereo school permit nephew fun</br>
}</br>

python3 bip39_check.py</br>
checks if all words are in the bip39 word list and shows their position</br>
{</br>
24w.txt Position: 1, BIP-39 Number: 1308</br>
24w.txt Position: 2, BIP-39 Number: 1426</br>
24w.txt Position: 3, BIP-39 Number: 760</br>
...</br>
24w.txt Position: 21, BIP-39 Number: 1543</br>
24w.txt Position: 22, BIP-39 Number: 1306</br>
24w.txt Position: 23, BIP-39 Number: 1187</br>
24w.txt Position: 24, BIP-39 Number: 753</br>
}</br>


python3 bip39_pack.py</br>
create 24wp.txt</br>
{</br>
Block: [1307, 1425, 759, 1488, 336, 300] -> Unique Number: 47114713094901367084 -> Combined Number: 4711471309490136708401 -> Encoded Number: rmbjt2wqa3j0oh</br>
Block: [1407, 1760, 16, 829, 92, 1471] -> Unique Number: 50723479794036696511 -> Combined Number: 5072347979403669651102 -> Encoded Number: tqhbl9wfx0gdy6</br>
Block: [328, 1531, 517, 101, 1729, 829] -> Unique Number: 11844383500477532989 -> Combined Number: 1184438350047753298903 -> Encoded Number: 6xyt29mlao5q6v</br>
Block: [244, 1708, 1542, 1305, 1186, 752] -> Unique Number: 8821087177546207984 -> Combined Number: 882108717754620798404 -> Encoded Number: 565ujnd5128c78</br>
Packed numbers saved to 24wp.txt</br>
}</br>

cat 24wp.txt</br>

rmbjt2wqa3j0oh</br>
tqhbl9wfx0gdy6</br>
6xyt29mlao5q6v</br>
565ujnd5128c78</br>

the order of the 4 blocks can be mixed(they have the order coded in the block)</br>


python3 bip39_unpack.py</br>
displays wordlist</br>
{</br>
Encoded Number: rmbjt2wqa3j0oh -> Combined Number: 4711471309490136708401 -> Sequence: 1 -> Unique Number: 47114713094901367084 -> Positions: [1307, 1425, 759, 1488, 336, 300] -> Block: ['pet', 'rate', 'galaxy', 'ring', 'claw', 'cereal']</br>
Encoded Number: tqhbl9wfx0gdy6 -> Combined Number: 5072347979403669651102 -> Sequence: 2 -> Unique Number: 50723479794036696511 -> Positions: [1407, 1760, 16, 829, 92, 1471] -> Block: ['quiz', 'swing', 'acoustic', 'guilt', 'argue', 'retire']</br>
Encoded Number: 6xyt29mlao5q6v -> Combined Number: 1184438350047753298903 -> Sequence: 3 -> Unique Number: 11844383500477532989 -> Positions: [328, 1531, 517, 101, 1729, 829] -> Block: ['cinnamon', 'satoshi', 'doll', 'arrow', 'subway', 'guilt']</br>
Encoded Number: 565ujnd5128c78 -> Combined Number: 882108717754620798404 -> Sequence: 4 -> Unique Number: 8821087177546207984 -> Positions: [244, 1708, 1542, 1305, 1186, 752] -> Block: ['burden', 'stereo', 'school', 'permit', 'nephew', 'fun']</br>

Decoded 24-word mnemonic:</br>
pet rate galaxy ring claw cereal quiz swing acoustic guilt argue retire cinnamon satoshi doll arrow subway guilt burden stereo school permit nephew fun</br>

Original 24-word mnemonic from 24w.txt:</br>
pet rate galaxy ring claw cereal quiz swing acoustic guilt argue retire cinnamon satoshi doll arrow subway guilt burden stereo school permit nephew fun</br>

Success: The decoded mnemonic matches the original mnemonic.</br>
}


python3 bip39_test.py 100</br>
Progress: |██████████████████████████████████████████████████| 100.0% Complete</br>

Success: All tests passed.</br>

test the algo for packing and unpacking


python3 bip39_qrcode.py</br>
generate qrcodes from the blocks in 24wp.txt and one combined qrcode</br>

Usage: bip39_qrcode_crypt.py <passphrase> <mode (GCM/CFB)>
python3 bip39_qrcode_crypt.py helloworld GCM</br>
{</br>
Combined QR code generated as combined_qr.png</br>
Combined encrypted block: R0NNOh01yEEq9WBa8gzqYdLQz9M7_6oW0ugey-VlXCeopX3pMKav41FXwM2mdBBZBx-4Wj-qUllmpkAmSpfNqSB2iujYxG88r3WlzSl5WgBPZw8pqwlcpDLL5_Za6Y-NeH7UUJY0kU6Fwus=</br>
QR code for block 1 generated as block_1_qr.png</br>
Encrypted block 1: R0NNOml6Q_3tVxLDU2uF6YiUkV_QwfqtM_BILF_i93f9DF0yxpUfneYvVN8EdsewHOfjJba-zznxu76e0NI=</br>
QR code for block 2 generated as block_2_qr.png</br>
Encrypted block 2: R0NNOvDgsqr9cphMhVhZc2Qj9s4pvfVqvyF2xIPnswmvzmbGTjN4FjlpwMakGfaooSgdGVez2VHz3IFVpnc=</br>
QR code for block 3 generated as block_3_qr.png</br>
Encrypted block 3: R0NNOv3uC-wZOSH7TzA9UWo3RVGYcJDmIScWQMrouOzA7-kUBunssDwWFVbPr93UZBW0_3MwE-vZDE18PtI=</br>
QR code for block 4 generated as block_4_qr.png</br>
Encrypted block 4: R0NNOihgwCjneJMge80PXf8-Xo05u8bU6LOqhlHvvOiUSU2l8ttxGmoYgxnvf1PVG1NZjO2QbalxwLVtQVQ=</br>
}</br>

Usage: bip39_decrypt.py <encrypted_data> <passphrase></br>
python3 bip39_decrypt.py "R0NNOh01yEEq9WBa8gzqYdLQz9M7_6oW0ugey-VlXCeopX3pMKav41FXwM2mdBBZBx-4Wj-qUllmpkAmSpfNqSB2iujYxG88r3WlzSl5WgBPZw8pqwlcpDLL5_Za6Y-NeH7UUJY0kU6Fwus=" "helloworld"
{</br>
Decrypted data: rmbjt2wqa3j0oh tqhbl9wfx0gdy6 6xyt29mlao5q6v 565ujnd5128c78</br>

Decoded 24-word mnemonic:</br>
pet rate galaxy ring claw cereal quiz swing acoustic guilt argue retire cinnamon satoshi doll arrow subway guilt burden stereo school permit nephew fun</br>

Original 24-word mnemonic from 24w.txt:</br>
pet rate galaxy ring claw cereal quiz swing acoustic guilt argue retire cinnamon satoshi doll arrow subway guilt burden stereo school permit nephew fun</br>

Success: The decoded mnemonic matches the original mnemonic.</br>
}</br>

just for the sake of completeness, but not a good idea, even though everything here in terms of scripts is possibly not a good idea:)</br>


use at your own risk!</br>
highly experimental!</br>
