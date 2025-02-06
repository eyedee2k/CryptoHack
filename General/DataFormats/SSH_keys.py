from Crypto.PublicKey import RSA

f = open('/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/DataFormats/bruce_rsa.pub', 'r')
pubkey = RSA.import_key(f.read())

print(pubkey.n)