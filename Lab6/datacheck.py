def get_bpp_from_corrupted_bmp(filename):
    """
    Reads a potentially corrupted BMP file and attempts to determine the bits per pixel (bpp).

    Args:
        filename (str): The path to the BMP file.

    Returns:
        int: The bits per pixel, or None if it cannot be determined.
    """
    try:
        with open(filename, "rb") as f:
            # Read the first 54 bytes (header size for most BMPs)
            header = f.read(54)

            # Check if the file is long enough to contain a basic header
            if len(header) < 54:
                print("Error: File is too small to be a valid BMP.")
                return None

            # Extract the bpp from the header (bytes 28-29)
            bpp = int.from_bytes(header[28:30], byteorder="little")
            return bpp

    except Exception as e:
        print(f"Error: Could not read or process the file: {e}")
        return None

# Example usage
filename = '/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/Lab6/aes.bmp.enc'
bpp = get_bpp_from_corrupted_bmp(filename)

if bpp:
    print(f"Bits per pixel: {bpp}")
else:
    print("Could not determine bits per pixel.")