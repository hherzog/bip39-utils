import qrcode

def read_encoded_blocks(file_path='24wp.txt'):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

def main():
    # Read the encoded blocks from 24wp.txt
    encoded_blocks = read_encoded_blocks('24wp.txt')

    # Option 1: Combine all blocks into one QR code
    combined_string = " ".join(encoded_blocks)
    generate_qr_code(combined_string, "combined_qr.png")
    print("Combined QR code generated as combined_qr.png")

    # Option 2: Generate separate QR codes for each block
    for i, block in enumerate(encoded_blocks):
        generate_qr_code(block, f"block_{i+1}_qr.png")
        print(f"QR code for block {i+1} generated as block_{i+1}_qr.png")

if __name__ == "__main__":
    main()
