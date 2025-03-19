def check_bmp_header(filename):
    with open(filename, 'rb') as f:
        header = f.read(2)
        if header == b'BM':
            print("Valid BMP header found.")
        else:
            print("Invalid BMP header.")

check_bmp_header('/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/Lab6/aes.bmp.enc') #replace path.