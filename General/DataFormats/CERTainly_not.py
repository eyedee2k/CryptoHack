from Crypto.PublicKey import RSA

key = RSA.importKey(open('/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/DataFormats/2048b-rsa-example-cert.der', 'rb').read())
print(key.n)

# https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html
# Variables on RSA key object:
# n (integer) – RSA modulus
# e (integer) – RSA public exponent
# d (integer) – RSA private exponent
# p (integer) – First factor of the RSA modulus
# q (integer) – Second factor of the RSA modulus
# invp (integer) – Chinese remainder component ()
# invq (integer) – Chinese remainder component ()
# u (integer) – Same as invp