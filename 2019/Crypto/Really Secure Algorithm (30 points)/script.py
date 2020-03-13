# If you know q,p,e and ciphertext and want to find and decrypt plaintext,this script is for you ;)

# Required library : pycryptodome

from Crypto.Util.number import inverse
from Crypto.Util.number import long_to_bytes


p = 8337989838551614633430029371803892077156162494012474856684174381868510024755832450406936717727195184311114937042673575494843631977970586746618123352329889
q = 7755060911995462151580541927524289685569492828780752345560845093073545403776129013139174889414744570087561926915046519199304042166351530778365529171009493
e = 65537

n = p*q

phi = (p - 1) * (q - 1)



d = inverse(e, phi)

print("d=",d,"\n")


ciphertext = 7022848098469230958320047471938217952907600532361296142412318653611729265921488278588086423574875352145477376594391159805651080223698576708934993951618464460109422377329972737876060167903857613763294932326619266281725900497427458047861973153012506595691389361443123047595975834017549312356282859235890330349

plaintext = pow(ciphertext, d, n) # (ciphertext^d) MOD n
print("plaintext = ",plaintext)


plaintext_hex_converted = hex(plaintext).split('x')[-1] # convert plaintext to hex

plaintext_from_hex_to_ascii = bytearray.fromhex(plaintext_hex_converted).decode() # convert hex to ascii

print("\nDecoded plaintext:",plaintext_from_hex_to_ascii)


################# Useful sources for the script #################
# https://github.com/JimChr-R4GN4R/picoCTF-writeups/blob/master/2019/Cryptography/rsa-pop-quiz%20(200%20points)/p-ct-e-n-_q-_phi-_d_pl.py
