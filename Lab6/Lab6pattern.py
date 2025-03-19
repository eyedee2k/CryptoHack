from PIL import Image
import io
import numpy as np

def read_bmp(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data

def detect_ecb_patterns(bmp_data):
    """
    Detects potential ECB mode patterns in a BMP image.

    Args:
        bmp_data: The raw bytes of the BMP image.

    Returns:
        A message indicating whether patterns were detected.
    """
    try:
        img = Image.open(io.BytesIO(bmp_data))
        img_array = np.array(img)
    except Exception as e:
        return f"Error opening image: {e}"

    block_size = 16  # AES block size in bytes. This is important.
    block_pixel_size = 16 #approximation, based on 3 bytes per pixel.

    height, width, channels = img_array.shape

    # Check for repeating blocks (simplified)
    block_counts = {}
    for y in range(0, height, block_pixel_size):
        for x in range(0, width, block_pixel_size):
            block = img_array[y:y + block_pixel_size, x:x + block_pixel_size]
            block_bytes = block.tobytes() #convert the pixel data into bytes.
            if len(block_bytes) < block_size * block_pixel_size * (channels/3): #handle edge cases.
                continue

            if block_bytes in block_counts:
                block_counts[block_bytes] += 1
            else:
                block_counts[block_bytes] = 1

    repeating_blocks = {block: count for block, count in block_counts.items() if count > 1}

    if repeating_blocks:
        return f"Possible ECB patterns detected: {len(repeating_blocks)} repeating blocks found."
    else:
        return "No obvious ECB patterns detected."

# Example usage (assuming bmp_data is your encrypted BMP bytes):
bmp_data = read_bmp('/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/Lab6/aes.bmp.enc') #or however you get your data.
pattern_message = detect_ecb_patterns(bmp_data)
print(pattern_message)