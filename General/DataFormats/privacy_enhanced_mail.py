from Crypto.PublicKey import RSA

with open('/Users/benjamin.brown/Documents/Uni/.venv/CryptoHack/DataFormats/privacy_enhanced_mail.pem') as key_file:
    key = key_file.read()
    rsa_key = RSA.importKey(key)
    rsa_key_vars = vars(rsa_key).keys()
    print(rsa_key_vars)
    print(rsa_key.d)

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