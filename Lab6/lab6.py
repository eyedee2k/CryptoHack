from PIL import Image
from Crypto.Cipher import AES
import io
import os

def decrypt_bmp_aes_ecb(encrypted_bmp_path, key, decrypted_bmp_path):
    """
    Decrypts a BMP image that was encrypted using AES ECB mode.

    Args:
        encrypted_bmp_path (str): Path to the encrypted BMP file.
        key (bytes): AES decryption key (16, 24, or 32 bytes).
        decrypted_bmp_path (str): Path to save the decrypted BMP file.
    """
    try:
        with open(encrypted_bmp_path, 'rb') as f_encrypted:
            encrypted_data = f_encrypted.read()

        cipher = AES(key, AES.MODE_ECB)
        decrypted_data = cipher.decrypt(encrypted_data)

        # Remove potential padding. This part is crucial and depends on how the original image was padded.
        # A common padding method is PKCS7.
        padding_length = decrypted_data[-1]
        if padding_length > 0 and padding_length <= AES.block_size:
            decrypted_data = decrypted_data[:-padding_length]

        # Attempt to load the decrypted data as an image
        try:
            img = Image.open(io.BytesIO(decrypted_data))
            img.save(decrypted_bmp_path)
            print(f"Decrypted image saved to {decrypted_bmp_path}")

        except Exception as image_err:
            print(f"Error opening or saving decrypted image: {image_err}")
            print("Decrypted data might not be a valid BMP, or padding was incorrectly removed.")
            # Optionally, you can write the raw decrypted data to a file for examination:
            # with open("decrypted_raw_data.bin", "wb") as f_raw:
            #     f_raw.write(decrypted_data)


    except FileNotFoundError:
        print(f"Error: Encrypted file not found at {encrypted_bmp_path}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
encrypted_bmp_file = '/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/Lab6/aes.bmp.enc'  # Replace with your encrypted BMP file
decrypted_bmp_file = '/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/Lab6/aes.bmp' # Replace with desired output path
key_bytes = b'YourSecretKey123'  # Replace with your AES key (16, 24, or 32 bytes)

if len(key_bytes) not in (16, 24, 32):
    print("Error: Key must be 16, 24, or 32 bytes long.")
else:
    decrypt_bmp_aes_ecb(encrypted_bmp_file, key_bytes, decrypted_bmp_file)