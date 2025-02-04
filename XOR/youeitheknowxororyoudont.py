import pwn

cipher_hex = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
cipher_bytes = bytes.fromhex(cipher_hex)
print(pwn.xor(cipher_bytes[0:7], bytes('crypto{','utf8')))  # return ==> myXORke
print(pwn.xor(cipher_bytes[-1], bytes('}', 'utf8'))) # return => y
key = bytes('myXORkey', 'utf8') # get 'myXORkey' according to above two line
flag = pwn.xor(key, cipher_bytes)
print('flag => ',flag.decode())