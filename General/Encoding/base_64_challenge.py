import base64

num = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
fromhex = bytes.fromhex(num)

print(base64.b64encode(fromhex))
