from Crypto.Util.number import inverse
import codecs

n = 99157116611790833573985267443453374677300242114595736901854871276546481648883
#g = 99157116611790833573985267443453374677300242114595736901854871276546481648884 # g = n + 1  (is not important here)
c = 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869

p = 310013024566643256138761337388255591613 # Find n primes from https://www.alpertron.com.ar/ECM.HTM
q = 319848228152346890121384041219876391791 #

phi = (p - 1) * (q - 1)


x = pow(c, phi, n ** 2) # x = (c^phi) MOD (n^2)

L = (x - 1) // n # L(x) = (x - 1) / n

mi = inverse(phi, n) # mi =  ( phi^(-1) ) MOD n

message = (L * mi) % n # message = ( L * mi ) MOD n

message_hexed = hex(message).replace('0x','') # Next we have to encode the message to hex. (we need to remove 0x to hex decode it)

message_from_hex_to_ascii = codecs.decode(message_hexed, "hex") # Next we convert hex to ascii and we take the plaintext


print(message_from_hex_to_ascii)


############## Useful sources for the script ##############
# https://en.wikipedia.org/wiki/Paillier_cryptosystem#Decryption
