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
24w.txt Position: 1, BIP-39 Number: 679</br>24w.txt Position: 2, BIP-39 Number: 1832</br>24w.txt Position: 3, BIP-39 Number: 1365</br>24w.txt Position: 4, BIP-39 Number: 1997</br>...</br>24w.txt Position: 21, BIP-39 Number: 1301</br>24w.txt Position: 22, BIP-39 Number: 1053</br>24w.txt Position: 23, BIP-39 Number: 1125</br>24w.txt Position: 24, BIP-39 Number: 196
}</br>
</br>
create 24wp.txt</br>
<b>python3 bip39_pack.py</b></br>
{
Block: [678, 1831, 1364, 1996, 1891, 367] -> Unique Number: 24459747396551383407 -> Combined Number: 2445974739655138340701 -> Encoded Number: ec7dapccclfuxp</br>Block: [1306, 28, 447, 1820, 2030, 1507] -> Unique Number: 47054105335314740707 -> Combined Number: 4705410533531474070702 -> Encoded Number: rl1i4950bps4vi</br>Block: [1475, 1960, 801, 124, 1776, 1335] -> Unique Number: 53176963168680248631 -> Combined Number: 5317696316868024863103 -> Encoded Number: v69d38xjcax6kf</br>Block: [408, 1972, 1300, 1052, 1124, 195] -> Unique Number: 14734452145946566851 -> Combined Number: 1473445214594656685104 -> Encoded Number: 8myjnkvjyuv774</br>Packed numbers saved to 24wp.txt
}</br>
</br>
<b>cat 24wp.txt</b></br>
{
ec7dapccclfuxp</br>rl1i4950bps4vi</br>v69d38xjcax6kf</br>8myjnkvjyuv774
}</br>
</br>
Info: The order of the 4 blocks can be mixed(they have the order coded in the block)</br>
</br>
</br>
displays unpacked wordlist from 24wp.txt</br>
<b>python3 bip39_unpack.py</b></br>
{
Encoded Number: ec7dapccclfuxp -> Combined Number: 2445974739655138340701 -> Sequence: 1 -> Unique Number: 24459747396551383407 -> Positions: [678, 1831, 1364, 1996, 1891, 367] -> Block: ['feel', 'top', 'pride', 'wet', 'unaware', 'combine']</br>Encoded Number: rl1i4950bps4vi -> Combined Number: 4705410533531474070702 -> Sequence: 2 -> Unique Number: 47054105335314740707 -> Positions: [1306, 28, 447, 1820, 2030, 1507] -> Block: ['person', 'adjust', 'dawn', 'toe', 'worry', 'round']</br>Encoded Number: v69d38xjcax6kf -> Combined Number: 5317696316868024863103 -> Sequence: 3 -> Unique Number: 53176963168680248631 -> Positions: [1475, 1960, 801, 124, 1776, 1335] -> Block: ['reveal', 'vital', 'goddess', 'auto', 'task', 'plunge']</br>Encoded Number: 8myjnkvjyuv774 -> Combined Number: 1473445214594656685104 -> Sequence: 4 -> Unique Number: 14734452145946566851 -> Positions: [408, 1972, 1300, 1052, 1124, 195] -> Block: ['credit', 'walk', 'penalty', 'logic', 'milk', 'blur']</br></br>Decoded 24-word mnemonic:</br>feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br></br>Original 24-word mnemonic from 24w.txt:</br>feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br></br>Success: The decoded mnemonic matches the original mnemonic.
}</br>
</br>
</br>
test the algo for packing and unpacking</br>
<b>python3 bip39_test.py 100</b></br>
{
Progress: |██████████████████████████████████████████████████| 100.0% Complete</br></br>Success: All tests passed.
}</br>
</br>
# other features</br>
<b>python3 bip39_pack.py --help</b></br>
{
Usage: python3 bip39_pack.py [passphrase] [mode] [QR]</br>If no passphrase and mode are provided, the data will be saved without encryption.</br>Modes: GCM, CFB</br>Optional 'QR' parameter to generate QR codes for encrypted blocks and combined encrypted block.
}</br>
</br>
<b>python3 bip39_pack.py "helloworld" GCM</b></br>
{
Block: [678, 1831, 1364, 1996, 1891, 367] -> Unique Number: 24459747396551383407 -> Combined Number: 2445974739655138340701 -> Encoded Number: ec7dapccclfuxp</br>Block: [1306, 28, 447, 1820, 2030, 1507] -> Unique Number: 47054105335314740707 -> Combined Number: 4705410533531474070702 -> Encoded Number: rl1i4950bps4vi</br>Block: [1475, 1960, 801, 124, 1776, 1335] -> Unique Number: 53176963168680248631 -> Combined Number: 5317696316868024863103 -> Encoded Number: v69d38xjcax6kf</br>Block: [408, 1972, 1300, 1052, 1124, 195] -> Unique Number: 14734452145946566851 -> Combined Number: 1473445214594656685104 -> Encoded Number: 8myjnkvjyuv774</br></br>Encrypted Blocks:</br>Encrypted block 1: R0NNOlNX0EizggmkmLRFJOaql4Xa9GL_wdM-oq-cuh8Aujq3mb-24-3YsNmSESs-ZMXw67C3axt5WGuE14g=</br>Encrypted block 2: R0NNOpKXkpeH1LKUuLTVIAGVHAz4aoOJIV7VHdWKrFbELrrOo0-GUUkLrpl1Jq7JAnL06F0bmCpX-g5KMR8=</br>Encrypted block 3: R0NNOsXliMiNfXv0nQyi2nNfUqEbo8r12tgwSBtPvzwew-lbcbX7v_HrnX5mrwWWMtwKn53KT7Ja1egfyCo=</br>Encrypted block 4: R0NNOucR0hpFv3oWwXGGI_GZWMkVzEoV3EcHw1A4NUmVRvgxJ1LaR8_XPkFGCqVBUbh1wPiu0l8guUsLwM8=</br></br>Combined Encrypted Block:</br>R0NNOqWh2yH3-WJp4Es6XGbX8pbDLr1eCoBTfZL1kqB5dw9ViOTHU2x7-WM_YFvvEs46qxCT61BWjmdM4yYOkLLcWTno_4eoyIHeMnkJHDTXm8e9kuDwcnwc6BgvT3ZyhWEz6i0elLSnIm4=
}</br>
</br>
# decrypt</br>
<b>python3 bip39_unpack.py --help</b></br>
{
Usage: python3 bip39_unpack.py [passphrase] [encrypted_data]</br>If no passphrase and encrypted data are provided, the data will be read without decryption.</br>Modes: GCM, CFB
}</br>
</br>
<b>python3 bip39_unpack.py "helloworld" R0NNOkHVzaE4vXDAB9FrovI7FzwehDvz7F33vXQJTUj22iKu6TBZe__k-5G8zpm2oPF51rRMfdfGwGv_hZxtPT3KTAAEkXBxEjGE8G1bs1yYRHWSH0R71lPOZXPyJ7yXN9eXx_GktrW60eE=</b></br>
{
Decrypted data: ec7dapccclfuxp</br>rl1i4950bps4vi</br>v69d38xjcax6kf</br>8myjnkvjyuv774</br>Encoded Number: ec7dapccclfuxp -> Combined Number: 2445974739655138340701 -> Sequence: 1 -> Unique Number: 24459747396551383407 -> Positions: [678, 1831, 1364, 1996, 1891, 367] -> Block: ['feel', 'top', 'pride', 'wet', 'unaware', 'combine']</br>Encoded Number: rl1i4950bps4vi -> Combined Number: 4705410533531474070702 -> Sequence: 2 -> Unique Number: 47054105335314740707 -> Positions: [1306, 28, 447, 1820, 2030, 1507] -> Block: ['person', 'adjust', 'dawn', 'toe', 'worry', 'round']</br>Encoded Number: v69d38xjcax6kf -> Combined Number: 5317696316868024863103 -> Sequence: 3 -> Unique Number: 53176963168680248631 -> Positions: [1475, 1960, 801, 124, 1776, 1335] -> Block: ['reveal', 'vital', 'goddess', 'auto', 'task', 'plunge']</br>Encoded Number: 8myjnkvjyuv774 -> Combined Number: 1473445214594656685104 -> Sequence: 4 -> Unique Number: 14734452145946566851 -> Positions: [408, 1972, 1300, 1052, 1124, 195] -> Block: ['credit', 'walk', 'penalty', 'logic', 'milk', 'blur']</br></br>Decoded 24-word mnemonic:</br>feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br></br>Original 24-word mnemonic from 24w.txt:</br>feel top pride wet unaware combine person adjust dawn toe worry round reveal vital goddess auto task plunge credit walk penalty logic milk blur</br></br>Success: The decoded mnemonic matches the original mnemonic.
}</br>
</br>
# sequential block decrypt</br>
<b>python3 bip39_unpack.py "helloworld" R0NNOm5T1y8Osi1GcJWuvmIm36NSgUBGd8mbypkeMvRHbawY5TaDooOF3l4Gk6retwKfoYaKRz7-wTqdlYI=</b></br>
{
Decrypted data: v69d38xjcax6kf</br>Encoded Number: v69d38xjcax6kf -> Combined Number: 5317696316868024863103 -> Sequence: 3 -> Unique Number: 53176963168680248631 -> Positions: [1475, 1960, 801, 124, 1776, 1335] -> Block: ['reveal', 'vital', 'goddess', 'auto', 'task', 'plunge']</br></br>Decoded block corresponding to sequence number:</br>Sequence: 3, Block: ['13 reveal', '14 vital', '15 goddess', '16 auto', '17 task', '18 plunge'], Positions: [1475, 1960, 801, 124, 1776, 1335]</br></br>Success: The decoded block matches the original mnemonic block.
}</br>
</br>
</br>
QR-Codes: will only be generated if encryption is used</br>
just for the sake of completeness, but not a good idea, even though everything here in terms of scripts is possibly not a good idea:)</br>
</br>
</br>
use at your own risk!</br>
highly experimental!</br>