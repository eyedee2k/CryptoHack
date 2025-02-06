import cv2

image1 = cv2.imread('/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/XOR/flag.png')
image2 = cv2.imread('/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/XOR/lemur.png')
dest_xor = cv2.bitwise_xor(image1, image2, mask=None)
cv2.imshow('Bitwise XOR', dest_xor)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()