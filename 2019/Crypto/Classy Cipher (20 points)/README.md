Every CTF starts off with a Caesar cipher, but we're more classy.

classy_cipher.py:

```
from secret import flag, shift

def encrypt(d, s):
	e = ''
	for c in d:
		e += chr((ord(c)+s) % 0xff)
	return e

assert encrypt(flag, shift) == ':<M?TLH8<A:KFBG@V'
```
#################################################################

So here we have a scipt that contains the ciphertext `:<M?TLH8<A:KFBG@V` .

If we check the script we can see that it's XOR encoding.

If we check `0xff` , this is the `255` number...So I was thinking to bruteforce it.

I made this script in python3:
```
ciphertext=':<M?TLH8<A:KFBG@V'
def decrypt(d, s):
	e = ''
	for c in d:
		e += chr((ord(c)+s) % 0xff)
	return e

for i in range(0, 256):
  flag = decrypt(ciphertext, i)

  print (i, flag)
```

At first I found this false flag: `ACTF[SO?CHARMING]` ...

But some lines down there was this flag: `actf{so_charming}` !

Flag: actf{so_charming}
