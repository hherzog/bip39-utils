# bip39 utils</br>
</br>
Packing 24-wordlists into blocks, based on the bip39 english.txt wordlist.</br>
In this example we create a wordlist, then pack it into 4 blocks</br>
and extract them later back to the 24-wordlist.</br>
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
python3 bip39_unique-wordlist.py</br>
{</br>
Mnemonic saved to 24w.txt:</br>
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br>
}</br>
</br>
checks if all words are in the bip39 word list and shows their position</br>
<b>python3 bip39_check.py</b></br>
{
24w.txt Position: 1, BIP-39 Number: 679
24w.txt Position: 2, BIP-39 Number: 1832
24w.txt Position: 3, BIP-39 Number: 1365
24w.txt Position: 4, BIP-39 Number: 1997
...
24w.txt Position: 21, BIP-39 Number: 1301
24w.txt Position: 22, BIP-39 Number: 1053
24w.txt Position: 23, BIP-39 Number: 1125
24w.txt Position: 24, BIP-39 Number: 196
}</br>
</br>
create 24wp.txt</br>
<b>python3 bip39_pack.py</b></br>
{
Block: [678, 1831, 1364, 1996, 1891, 367] -> Unique Number: 24459747396551383407 -> Combined Number: 2445974739655138340701 -> Encoded Number: ec7dapccclfuxp
Block: [1306, 28, 447, 1820, 2030, 1507] -> Unique Number: 47054105335314740707 -> Combined Number: 4705410533531474070702 -> Encoded Number: rl1i4950bps4vi
Block: [1475, 1960, 801, 124, 1776, 1335] -> Unique Number: 53176963168680248631 -> Combined Number: 5317696316868024863103 -> Encoded Number: v69d38xjcax6kf
Block: [408, 1972, 1300, 1052, 1124, 195] -> Unique Number: 14734452145946566851 -> Combined Number: 1473445214594656685104 -> Encoded Number: 8myjnkvjyuv774
Packed numbers saved to 24wp.txt
}</br>
</br>
<b>cat 24wp.txt</b></br>
{
ec7dapccclfuxp
rl1i4950bps4vi
v69d38xjcax6kf
8myjnkvjyuv774
}</br>
</br>
Info: The order of the 4 blocks can be mixed(they have the order coded in the block)</br>
</br>
</br>
displays unpacked wordlist from 24wp.txt</br>
<b>python3 bip39_unpack.py</b></br>
{
Encoded Number: ec7dapccclfuxp -> Combined Number: 2445974739655138340701 -> Sequence: 1 -> Unique Number: 24459747396551383407 -> Positions: [678, 1831, 1364, 1996, 1891, 367] -> Block: ['feel', 'top', 'pride', 'wet', 'unaware', 'combine']
Encoded Number: rl1i4950bps4vi -> Combined Number: 4705410533531474070702 -> Sequence: 2 -> Unique Number: 47054105335314740707 -> Positions: [1306, 28, 447, 1820, 2030, 1507] -> Block: ['person', 'adjust', 'dawn', 'toe', 'worry', 'round']
Encoded Number: v69d38xjcax6kf -> Combined Number: 5317696316868024863103 -> Sequence: 3 -> Unique Number: 53176963168680248631 -> Positions: [1475, 1960, 801, 124, 1776, 1335] -> Block: ['reveal', 'vital', 'goddess', 'auto', 'task', 'plunge']
Encoded Number: 8myjnkvjyuv774 -> Combined Number: 1473445214594656685104 -> Sequence: 4 -> Unique Number: 14734452145946566851 -> Positions: [408, 1972, 1300, 1052, 1124, 195] -> Block: ['credit', 'walk', 'penalty', 'logic', 'milk', 'blur']

Decoded 24-word mnemonic:
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur

Original 24-word mnemonic from 24w.txt:
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur

Success: The decoded mnemonic matches the original mnemonic.
}</br>
</br>
</br>
test the algo for packing and unpacking</br>
<b>python3 bip39_test.py 100</b></br>
{
Progress: |██████████████████████████████████████████████████| 100.0% Complete

Success: All tests passed.
}</br>
</br>
# other features</br>
<b>python3 bip39_pack.py --help</b></br>
{
Usage: python3 bip39_pack.py [passphrase] [mode] [QR]
If no passphrase and mode are provided, the data will be saved without encryption.
Modes: GCM, CFB
Optional 'QR' parameter to generate QR codes for encrypted blocks and combined encrypted block.
}</br>
</br>
<b>python3 bip39_pack.py "helloworld" GCM</b></br>
{
Block: [678, 1831, 1364, 1996, 1891, 367] -> Unique Number: 24459747396551383407 -> Combined Number: 2445974739655138340701 -> Encoded Number: ec7dapccclfuxp
Block: [1306, 28, 447, 1820, 2030, 1507] -> Unique Number: 47054105335314740707 -> Combined Number: 4705410533531474070702 -> Encoded Number: rl1i4950bps4vi
Block: [1475, 1960, 801, 124, 1776, 1335] -> Unique Number: 53176963168680248631 -> Combined Number: 5317696316868024863103 -> Encoded Number: v69d38xjcax6kf
Block: [408, 1972, 1300, 1052, 1124, 195] -> Unique Number: 14734452145946566851 -> Combined Number: 1473445214594656685104 -> Encoded Number: 8myjnkvjyuv774

Encrypted Blocks:
Encrypted block 1: R0NNOsIFDJ9IJMK789wCCKspZRUqB3dHURTarB8oPQfg4oBekzRUCB4wUNGYFO7tVtM10b3VqlqYdKzIwdA=
Encrypted block 2: R0NNOhji7HjSLrI6JZmBzhPJ2Q9pVZkrOaJsIx-h4i4HtUt7E-z0iWViTWptHnDDAranV8pzRDtJDW0Qxg0=
Encrypted block 3: R0NNOunAWTsUFbHTx7gkWrChKD1Kd7x0cB91fzU8ChDXK0HknRic1IZfN5jEn15QJkPb_s_DatRbi5M79QQ=
Encrypted block 4: R0NNOuWIzBhTV154SI4PqshnUNeCNls3FOZlHduhun__AovVxPvECerb-VrdpIFpl7BVWTqMu_EnNjGmblM=

Combined Encrypted Block:
R0NNOk_yU-yjem9huUDdu3lIth4-0ycpGoiTwOAzffwgZPtsohLmfMTtZfnyWKMtEm28cWPWkkkQtBlnoeKsnnf294bg7CarIsFhJXBMbf7RXDQkuNohZ7mEX3ajNkSl51BhWP2CWH9JBu8=
}</br>
</br>
# decrypt</br>
<b>python3 bip39_unpack.py --help</b></br>
{
Usage: python3 bip39_unpack.py [passphrase] [encrypted_data]
If no passphrase and encrypted data are provided, the data will be read without decryption.
Modes: GCM, CFB
}</br>
</br>
<b>python3 bip39_unpack.py "helloworld" R0NNOkHVzaE4vXDAB9FrovI7FzwehDvz7F33vXQJTUj22iKu6TBZe__k-5G8zpm2oPF51rRMfdfGwGv_hZxtPT3KTAAEkXBxEjGE8G1bs1yYRHWSH0R71lPOZXPyJ7yXN9eXx_GktrW60eE=</b></br>
{
Decrypted data: ec7dapccclfuxp
rl1i4950bps4vi
v69d38xjcax6kf
8myjnkvjyuv774
Encoded Number: ec7dapccclfuxp -> Combined Number: 2445974739655138340701 -> Sequence: 1 -> Unique Number: 24459747396551383407 -> Positions: [678, 1831, 1364, 1996, 1891, 367] -> Block: ['feel', 'top', 'pride', 'wet', 'unaware', 'combine']
Encoded Number: rl1i4950bps4vi -> Combined Number: 4705410533531474070702 -> Sequence: 2 -> Unique Number: 47054105335314740707 -> Positions: [1306, 28, 447, 1820, 2030, 1507] -> Block: ['person', 'adjust', 'dawn', 'toe', 'worry', 'round']
Encoded Number: v69d38xjcax6kf -> Combined Number: 5317696316868024863103 -> Sequence: 3 -> Unique Number: 53176963168680248631 -> Positions: [1475, 1960, 801, 124, 1776, 1335] -> Block: ['reveal', 'vital', 'goddess', 'auto', 'task', 'plunge']
Encoded Number: 8myjnkvjyuv774 -> Combined Number: 1473445214594656685104 -> Sequence: 4 -> Unique Number: 14734452145946566851 -> Positions: [408, 1972, 1300, 1052, 1124, 195] -> Block: ['credit', 'walk', 'penalty', 'logic', 'milk', 'blur']

Decoded 24-word mnemonic:
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur

Original 24-word mnemonic from 24w.txt:
feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur

Success: The decoded mnemonic matches the original mnemonic.
}</br>
</br>
# sequential block decrypt</br>
<b>python3 bip39_unpack.py "helloworld" R0NNOm5T1y8Osi1GcJWuvmIm36NSgUBGd8mbypkeMvRHbawY5TaDooOF3l4Gk6retwKfoYaKRz7-wTqdlYI=</b></br>
{
Decrypted data: v69d38xjcax6kf
Encoded Number: v69d38xjcax6kf -> Combined Number: 5317696316868024863103 -> Sequence: 3 -> Unique Number: 53176963168680248631 -> Positions: [1475, 1960, 801, 124, 1776, 1335] -> Block: ['reveal', 'vital', 'goddess', 'auto', 'task', 'plunge']

Decoded block corresponding to sequence number:
Sequence: 3, Block: ['13 reveal', '14 vital', '15 goddess', '16 auto', '17 task', '18 plunge'], Positions: [1475, 1960, 801, 124, 1776, 1335]

Success: The decoded block matches the original mnemonic block.
}</br>
</br>
</br>
QR-Codes: will only be generated if encryption is used</br>
</br>
<b>python3 bip39_pack.py "helloworld" GCM QR</b></br>
{
Block: [678, 1831, 1364, 1996, 1891, 367] -> Unique Number: 24459747396551383407 -> Combined Number: 2445974739655138340701 -> Encoded Number: ec7dapccclfuxp
Block: [1306, 28, 447, 1820, 2030, 1507] -> Unique Number: 47054105335314740707 -> Combined Number: 4705410533531474070702 -> Encoded Number: rl1i4950bps4vi
Block: [1475, 1960, 801, 124, 1776, 1335] -> Unique Number: 53176963168680248631 -> Combined Number: 5317696316868024863103 -> Encoded Number: v69d38xjcax6kf
Block: [408, 1972, 1300, 1052, 1124, 195] -> Unique Number: 14734452145946566851 -> Combined Number: 1473445214594656685104 -> Encoded Number: 8myjnkvjyuv774

Encrypted Blocks:
Encrypted block 1: R0NNOvFutBBi9YM9yyyPggSXGUbC_ixLzK-Jj5e1gtyGjtwAWl88GNt3Dn7XxG1PpKgT7U86cOW7TUobmkc=
QR code for block 1 generated as block_1_qr.png
Encrypted block 2: R0NNOs_nBBFOwq-2w4Fu0MM0CGTvQMTdIKK-Dgnh1ehEWjK-gaY3Lyr-vvQfhDrTWI9ohGnpgLbWPIPqBug=
QR code for block 2 generated as block_2_qr.png
Encrypted block 3: R0NNOvhCNHtScASmCb-36Nueu9QnQXGpsKcxU2jzUx_f00HkXshQihopAAgyjN6LXn3phtou-Pz28ao_Nvs=
QR code for block 3 generated as block_3_qr.png
Encrypted block 4: R0NNOhFamMMMiwO7PWhe4snifrbrFiGBms8ErCzJfFlcCqVW51GRYeEMO7o5eEkb9KnDk6TPIo0Ek_1hIcc=
QR code for block 4 generated as block_4_qr.png

Combined Encrypted Block:
R0NNOlEac5ZZCDKIqstLU74LUeu62tMy_3H7P7trDq2W-OHWxcZjdCsnOS4Z1HVHDJome9UcOtukH71jQPjGndutKT2hAH2FXsLBPQLMKHr8grcilB9cc6K8aAe0fUWDz2eCQmb1zC6pyN0=
Combined QR code generated as combined_qr.png
}</br>
</br>
<div style="display: flex; flex-wrap: wrap;"><img src="block_1_qr.png" alt="block_1_qr.png" style="width:45px; height:45px; margin-right: 10px; margin-bottom: 10px;" /><img src="block_2_qr.png" alt="block_2_qr.png" style="width:45px; height:45px; margin-right: 10px; margin-bottom: 10px;" /><img src="block_3_qr.png" alt="block_3_qr.png" style="width:45px; height:45px; margin-right: 10px; margin-bottom: 10px;" /><img src="block_4_qr.png" alt="block_4_qr.png" style="width:45px; height:45px; margin-right: 10px; margin-bottom: 10px;" /><img src="combined_qr.png" alt="combined_qr.png" style="width:53px; height:53px; margin-right: 10px; margin-bottom: 10px;" /></div>
</br>
just for the sake of completeness, but not a good idea, even though everything here in terms of scripts is possibly not a good idea:)</br>
</br>
</br>
use at your own risk!</br>
highly experimental!</br>