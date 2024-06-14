# bip39 utils</br>
</br>
Creating a 24-word list from the bip39 English word list, then packing it into 4 blocks and extracting them back.</br>
</br>
How to use:</br>
</br>
Source of the bip39 wordlist:</br>
https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt</br>
https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt</br>
</br>
wget https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt</br>
</br>
</br>
create 24w.txt</br>
Warning! Overwrites existing 24w.txt. Use only for generating and testing scripts.</br>
</br>
python3 bip39_unique-wordlist.py</br>
{</br>
Mnemonic saved to 24w.txt:</br>
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br>
}</br>
</br>
Verifies that all words are in the bip39 word list and displays their positions.</br>
</br>
<b>python3 bip39_check.py</b></br>
{</br>
24w.txt Position: 1, BIP-39 Number: 679</br>
24w.txt Position: 2, BIP-39 Number: 1832</br>
24w.txt Position: 3, BIP-39 Number: 1365</br>
24w.txt Position: 4, BIP-39 Number: 1997</br>
...</br>
24w.txt Position: 21, BIP-39 Number: 1301</br>
24w.txt Position: 22, BIP-39 Number: 1053</br>
24w.txt Position: 23, BIP-39 Number: 1125</br>
24w.txt Position: 24, BIP-39 Number: 196</br>
}</br>
</br>
create 24wp.txt</br>
<b>python3 bip39_pack.py</b></br>
{</br>
Block: [678, 1831, 1364, 1996, 1891, 367] -> Unique Number: 24459747396551383407 -> Combined Number: 2445974739655138340701 -> Encoded Number: ec7dapccclfuxp</br>
Block: [1306, 28, 447, 1820, 2030, 1507] -> Unique Number: 47054105335314740707 -> Combined Number: 4705410533531474070702 -> Encoded Number: rl1i4950bps4vi</br>
Block: [1475, 1960, 801, 124, 1776, 1335] -> Unique Number: 53176963168680248631 -> Combined Number: 5317696316868024863103 -> Encoded Number: v69d38xjcax6kf</br>
Block: [408, 1972, 1300, 1052, 1124, 195] -> Unique Number: 14734452145946566851 -> Combined Number: 1473445214594656685104 -> Encoded Number: 8myjnkvjyuv774</br>
Packed numbers saved to 24wp.txt</br>
}</br>
</br>
<b>cat 24wp.txt</b></br>
{</br>
ec7dapccclfuxp</br>
rl1i4950bps4vi</br>
v69d38xjcax6kf</br>
8myjnkvjyuv774</br>
}</br>
</br>
The 4 blocks can be reordered as they have their order encoded.</br>
</br>
Shows the unpacked wordlist from 24wp.txt.</br>
<b>python3 bip39_unpack.py</b></br>
{</br>
Encoded Number: ec7dapccclfuxp -> Combined Number: 2445974739655138340701 -> Sequence: 1 -> Unique Number: 24459747396551383407 -> Positions: [678, 1831, 1364, 1996, 1891, 367] -> Block: ['feel', 'top', 'pride', 'wet', 'unaware', 'combine']</br>
Encoded Number: rl1i4950bps4vi -> Combined Number: 4705410533531474070702 -> Sequence: 2 -> Unique Number: 47054105335314740707 -> Positions: [1306, 28, 447, 1820, 2030, 1507] -> Block: ['person', 'adjust', 'dawn', 'toe', 'worry', 'round']</br>
Encoded Number: v69d38xjcax6kf -> Combined Number: 5317696316868024863103 -> Sequence: 3 -> Unique Number: 53176963168680248631 -> Positions: [1475, 1960, 801, 124, 1776, 1335] -> Block: ['reveal', 'vital', 'goddess', 'auto', 'task', 'plunge']</br>
Encoded Number: 8myjnkvjyuv774 -> Combined Number: 1473445214594656685104 -> Sequence: 4 -> Unique Number: 14734452145946566851 -> Positions: [408, 1972, 1300, 1052, 1124, 195] -> Block: ['credit', 'walk', 'penalty', 'logic', 'milk', 'blur']</br>
</br>
Decoded 24-word mnemonic:</br>
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br>
</br>
Original 24-word mnemonic from 24w.txt:</br>
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br>
</br>
Success: The decoded mnemonic matches the original mnemonic.</br>
}</br>
</br>
Tests the algorithm for packing and unpacking.</br>
</br>
<b>python3 bip39_test.py 100</b></br>
{</br>
Progress: |██████████████████████████████████████████████████| 100.0% Complete</br>
</br>
Success: All tests passed.</br>
}</br>
</br>
# other features</br>
<b>python3 bip39_pack.py --help</b></br>
{</br>
Usage: python3 bip39_pack.py [passphrase] [mode] [QR]</br>
If no passphrase and mode are provided, the data will be saved without encryption.</br>
Modes: GCM, CFB</br>
Optional 'QR' parameter to generate QR codes for encrypted blocks and combined encrypted block.</br>
}</br>
</br>
<b>python3 bip39_pack.py "helloworld" GCM</b></br>
{</br>
Block: [678, 1831, 1364, 1996, 1891, 367] -> Unique Number: 24459747396551383407 -> Combined Number: 2445974739655138340701 -> Encoded Number: ec7dapccclfuxp</br>
Block: [1306, 28, 447, 1820, 2030, 1507] -> Unique Number: 47054105335314740707 -> Combined Number: 4705410533531474070702 -> Encoded Number: rl1i4950bps4vi</br>
Block: [1475, 1960, 801, 124, 1776, 1335] -> Unique Number: 53176963168680248631 -> Combined Number: 5317696316868024863103 -> Encoded Number: v69d38xjcax6kf</br>
Block: [408, 1972, 1300, 1052, 1124, 195] -> Unique Number: 14734452145946566851 -> Combined Number: 1473445214594656685104 -> Encoded Number: 8myjnkvjyuv774</br>
</br>
Encrypted Blocks:</br>
Encrypted block 1: R0NNOhw-JtQyit57nAI2oDs6X-G-k2_RyWG5F6Gpu9hTtijNN4jGnjCLKb4HuuQ6k1yOVVKWk9ri-cMtIvA=</br>
Encrypted block 2: R0NNOsmhozSK6sIIk0gFwKq5UqOcMXIgzsgeJxPlsYkYAVqls5Bsd-00A5eH0VJqv_3Req173rEpKquvXJ0=</br>
Encrypted block 3: R0NNOuQrIo0RVtA18eGjynPkmAawhyZdZqy_646ZK51gCMXIImH4FUvSR8HIIHDfG2_5-JVQ7jMJJxA9F7E=</br>
Encrypted block 4: R0NNOhTgDWxOkhLz3B_O-SOf27JQSz2akfB2lfgA3Sn7wqDOgG7qUusUYKd9s_WcpQ5lNDD_jUCAcQPdjm4=</br>
</br>
Combined Encrypted Block:</br>
R0NNOp-kd2w6Vorfc_KNbRcPNH49lKGGKXAEPs41vtHZKU1eDDeGS9M308adILR4GbTn1IgNPSE_G7KIV9i8VBfaW0h_JNubNDjR7Z6428NTMxGHrV2zS8kq1VRdAoZL9jqVjV7xm-xO4M8=</br>
}</br>
</br>
# decrypt</br>
<b>python3 bip39_unpack.py --help</b></br>
{</br>
Usage: python3 bip39_unpack.py [passphrase] [encrypted_data]</br>
If no passphrase and encrypted data are provided, the data will be read without decryption.</br>
Modes: GCM, CFB</br>
}</br>
</br>
<b>python3 bip39_unpack.py "helloworld" R0NNOkHVzaE4vXDAB9FrovI7FzwehDvz7F33vXQJTUj22iKu6TBZe__k-5G8zpm2oPF51rRMfdfGwGv_hZxtPT3KTAAEkXBxEjGE8G1bs1yYRHWSH0R71lPOZXPyJ7yXN9eXx_GktrW60eE=</b></br>
{</br>
Decrypted data: ec7dapccclfuxp</br>
rl1i4950bps4vi</br>
v69d38xjcax6kf</br>
8myjnkvjyuv774</br>
Encoded Number: ec7dapccclfuxp -> Combined Number: 2445974739655138340701 -> Sequence: 1 -> Unique Number: 24459747396551383407 -> Positions: [678, 1831, 1364, 1996, 1891, 367] -> Block: ['feel', 'top', 'pride', 'wet', 'unaware', 'combine']</br>
Encoded Number: rl1i4950bps4vi -> Combined Number: 4705410533531474070702 -> Sequence: 2 -> Unique Number: 47054105335314740707 -> Positions: [1306, 28, 447, 1820, 2030, 1507] -> Block: ['person', 'adjust', 'dawn', 'toe', 'worry', 'round']</br>
Encoded Number: v69d38xjcax6kf -> Combined Number: 5317696316868024863103 -> Sequence: 3 -> Unique Number: 53176963168680248631 -> Positions: [1475, 1960, 801, 124, 1776, 1335] -> Block: ['reveal', 'vital', 'goddess', 'auto', 'task', 'plunge']</br>
Encoded Number: 8myjnkvjyuv774 -> Combined Number: 1473445214594656685104 -> Sequence: 4 -> Unique Number: 14734452145946566851 -> Positions: [408, 1972, 1300, 1052, 1124, 195] -> Block: ['credit', 'walk', 'penalty', 'logic', 'milk', 'blur']</br>
</br>
Decoded 24-word mnemonic:</br>
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br>
</br>
Original 24-word mnemonic from 24w.txt:</br>
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br>
</br>
Success: The decoded mnemonic matches the original mnemonic.</br>
}</br>
</br>
# sequential block decrypt</br>
<b>python3 bip39_unpack.py "helloworld" R0NNOm5T1y8Osi1GcJWuvmIm36NSgUBGd8mbypkeMvRHbawY5TaDooOF3l4Gk6retwKfoYaKRz7-wTqdlYI=</b></br>
{</br>
Decrypted data: v69d38xjcax6kf</br>
Encoded Number: v69d38xjcax6kf -> Combined Number: 5317696316868024863103 -> Sequence: 3 -> Unique Number: 53176963168680248631 -> Positions: [1475, 1960, 801, 124, 1776, 1335] -> Block: ['reveal', 'vital', 'goddess', 'auto', 'task', 'plunge']</br>
</br>
Decoded block corresponding to sequence number:</br>
Sequence: 3, Block: ['13 reveal', '14 vital', '15 goddess', '16 auto', '17 task', '18 plunge'], Positions: [1475, 1960, 801, 124, 1776, 1335]</br>
</br>
Success: The decoded block matches the original mnemonic block.</br>
}</br>
</br>
QR codes are generated only when encryption is used.</br>
</br>
<b>python3 bip39_pack.py "helloworld" GCM QR</b></br>
{</br>
Block: [678, 1831, 1364, 1996, 1891, 367] -> Unique Number: 24459747396551383407 -> Combined Number: 2445974739655138340701 -> Encoded Number: ec7dapccclfuxp</br>
Block: [1306, 28, 447, 1820, 2030, 1507] -> Unique Number: 47054105335314740707 -> Combined Number: 4705410533531474070702 -> Encoded Number: rl1i4950bps4vi</br>
Block: [1475, 1960, 801, 124, 1776, 1335] -> Unique Number: 53176963168680248631 -> Combined Number: 5317696316868024863103 -> Encoded Number: v69d38xjcax6kf</br>
Block: [408, 1972, 1300, 1052, 1124, 195] -> Unique Number: 14734452145946566851 -> Combined Number: 1473445214594656685104 -> Encoded Number: 8myjnkvjyuv774</br>
</br>
Encrypted Blocks:</br>
Encrypted block 1: R0NNOj62epwBdCHelFkKLJLCxh7Zg57JlKUTBemq_4M65wgwxeBeR-QLvCMhjUVBWq3y_8qbYeB6kAqxE2o=</br>
QR code for block 1 generated as block_1_qr.png</br>
Encrypted block 2: R0NNOg3TVv7eGlqOF1L6LSeFxGfaq4AtnqVv3c-EWPqH8XkilELC6QoCCj81K1dMhId0RowWgjJQ95gKJEw=</br>
QR code for block 2 generated as block_2_qr.png</br>
Encrypted block 3: R0NNOvpSELy7OQ9FYqQGcqo3DBAKcjDnl1qKntWF4bSK1Sd7u0dhxotUr-IcQX8wEfxrcE5oCiJO2IHIMmc=</br>
QR code for block 3 generated as block_3_qr.png</br>
Encrypted block 4: R0NNOh6LdZVyC9Qv88Bum4g5sYqkqsUjSxlTOHA6OaTtohnqjn_YdvQtZ8nbL-QXw3zZK09ca8TwbslEJHY=</br>
QR code for block 4 generated as block_4_qr.png</br>
</br>
Combined Encrypted Block:</br>
R0NNOo9f1eeWneVEU5ou9Ou6H71piAS9O2fsIFIOmLSyh61pBuyeg8eLpzC86ho8K3FTJvGD9jjVbqF94v5KswS_KYwUcWDAgsJAIutbadc5rpmbQyDYbwUIs1oA3K652jXKS5z2Eepz1VU=</br>
Combined QR code generated as combined_qr.png</br>
}</br>
</br>
<div><img src="block_1_qr.png" alt="block_1_qr.png" width="157.5px" height="157.5px" style="width:157.5px; height:157.5px; margin-right: 10px; margin-bottom: 10px; display:inline-block; vertical-align:top;" /><img src="block_2_qr.png" alt="block_2_qr.png" width="157.5px" height="157.5px" style="width:157.5px; height:157.5px; margin-right: 10px; margin-bottom: 10px; display:inline-block; vertical-align:top;" /><img src="block_3_qr.png" alt="block_3_qr.png" width="157.5px" height="157.5px" style="width:157.5px; height:157.5px; margin-right: 10px; margin-bottom: 10px; display:inline-block; vertical-align:top;" /><img src="block_4_qr.png" alt="block_4_qr.png" width="157.5px" height="157.5px" style="width:157.5px; height:157.5px; margin-right: 10px; margin-bottom: 10px; display:inline-block; vertical-align:top;" /></div>
<div><img src="combined_qr.png" alt="combined_qr.png" width="185.5px" height="185.5px" style="width:185.5px; height:185.5px; margin-right: 10px; margin-bottom: 10px; display:inline-block; vertical-align:top;" /></div>
</br>
For completeness, but using these scripts might not be a good idea. Use at your own risk! Highly experimental!</br>
