The year is 20XX. 

ångstromCTF only has pwn challenges, and the winner is solely determined by who can establish a socket connection first. 

In the data remnants of an ancient hard disk, we've recovered a string of letters and digits. 

The only clue is the etching on the disk's surface: Paillier.


flag.txt:
```
n = 99157116611790833573985267443453374677300242114595736901854871276546481648883
g = 99157116611790833573985267443453374677300242114595736901854871276546481648884
c = 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869
```

################################################################################

So from the clue we can see that this is Paillier cryptosystem.

If we search,we can find in wikipedia everything we need to solve this challenge.

https://en.wikipedia.org/wiki/Paillier_cryptosystem#Decryption

( It's like RSA cryptosystem)

Here we have `n = p * q` , `g = n + 1` and `c` .

From wikipedia we can find this:
- The public (encryption) key is `n`,`g`
- The private (decryption) key is `L`,`mi`

So we need to find `L` and `mi` ...

Here are all the equations we need to find L:
`L(x) = (x - 1) / n`
`x = (c^phi) MOD (n^2)`
`phi = (p - 1) * (q - 1)`

So first we have to find `phi`,so I used https://www.alpertron.com.ar/ECM.HTM and put n in ther and pressed 'Factor' button.

You have to be patient,because it will take around 3 minutes to find `n`'s primals.

You can find it faster if you put n value here: http://factordb.com/

So we will see that `p = 310013024566643256138761337388255591613` and `q = 319848228152346890121384041219876391791`

So from here we can find `phi = (p - 1) * (q - 1)`

Next we can find `x = (c^phi) MOD (n^2)` 

And finally `L(x) = (x - 1) / n`

Next we have to find `mi = ( phi^(-1) ) MOD n`

And then we can find `message = ( L * mi ) MOD n`

Then we have to encode in hex the message and then convert it to ascii (as like in RSA decryption way).

I made a script in python3 for this,so just put in there the required values (with p and q) and then open terminal and type `python3 script.py`

Flag: actf{crypto_lives}
