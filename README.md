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
Encrypted block 1: R0NNOl99vpHGUQt9uuQI7ezwbaKKOD8ImPBlp8Foh4epNmV1EhhgNfo35XvJfQM6o3KlQl2CMMfkrCv3U0g=</br>
Encrypted block 2: R0NNOop3ECaBqjur16pN8iC0rfTfxXFvaQsToyfOyjSdqe_8urpvsaNBh78kJxo2__YikGPG6wtxrAdPntI=</br>
Encrypted block 3: R0NNOoQ_nrEIf1XY64rakMmRtP0kR9qRqZrRh0rx6-Uof9FYZ_3mudmu74sFCBVgLrLh_imNvYZMvbdYios=</br>
Encrypted block 4: R0NNOoueFmMs1w3LIw9HdBlY7T69Efyh-LRpIyHx2xrRBFZujEwCsgzpltu02QjomQb_5NshaEJWnwohgbM=</br>
</br>
Combined Encrypted Block:</br>
R0NNOnj9d_gdYzLg9bbcqqaWGOYlmeN3kSy9iQLw6S09jXdJF_S-ea66kSFtN9InFXOi67gj8RBK5Ha9xne9d8AoWbMneZvo-zhCNL1uI_ltC3GY26jWJECyc9i7PmVSJyP4EVL43SMSj5A=</br>
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
Encrypted block 1: R0NNOsUwW1nd5T9T_FtngyAK5gTnVBcKLfZ7JafvSOOgH-po12NE34akYvxAZQylkl5k6ForZWeq9JLbsXQ=</br>
QR code for block 1 generated as block_1_qr.png</br>
Encrypted block 2: R0NNOqj4akTFI9YenhDmbAxNOZv-DrL8Xet23OARdy2N8YC_TIj_mmzm2izYItA8xngIr8sNUKSpQiDlvXY=</br>
QR code for block 2 generated as block_2_qr.png</br>
Encrypted block 3: R0NNOveFZj8QHxAblkF_7HH8P-rujy08rrGAeGJTfh8MIOeAMs9i92xWGfkHFQLVbhKNc5z9KabjegvdK58=</br>
QR code for block 3 generated as block_3_qr.png</br>
Encrypted block 4: R0NNOqdiw3i7VnxFwFegDIf2TTGTVFAAKF5OUXKuBgXC0lihUz129TqYKItmoiaIeJ_rtpe4t_xzv-lvKwk=</br>
QR code for block 4 generated as block_4_qr.png</br>
</br>
Combined Encrypted Block:</br>
R0NNOmVaMNOVfVurnTgDQYWWhfyQIV6efDssRe9bwDKjvplmosjObkRQ9vtqqjuwmKPEVKJX08eKGBpP-vzo8lDkI7XzGDXXAHwOUAfIIf-xs2qWRZkyK2Et3UxzQtxwlThp1o6xedLZjKw=</br>
Combined QR code generated as combined_qr.png</br>
}</br>
</br>
<div style="display: flex; flex-wrap: wrap;"><img src="block_1_qr.png" alt="block_1_qr.png" style="width:157.5px; height:157.5px; margin-right: 10px; margin-bottom: 10px;" /><img src="block_2_qr.png" alt="block_2_qr.png" style="width:157.5px; height:157.5px; margin-right: 10px; margin-bottom: 10px;" /><img src="block_3_qr.png" alt="block_3_qr.png" style="width:157.5px; height:157.5px; margin-right: 10px; margin-bottom: 10px;" /><img src="block_4_qr.png" alt="block_4_qr.png" style="width:157.5px; height:157.5px; margin-right: 10px; margin-bottom: 10px;" /></div></br>
<div style="display: flex; flex-wrap: wrap;"><img src="combined_qr.png" alt="combined_qr.png" style="width:185.5px; height:185.5px; margin-right: 10px; margin-bottom: 10px;" /></div></br>
</br>
For completeness, but using these scripts might not be a good idea. Use at your own risk! Highly experimental!</br>
