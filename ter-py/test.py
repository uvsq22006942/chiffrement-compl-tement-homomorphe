import numpy as np
from util   import *
from keygen import keygen
from enc    import encrypt
from dec    import decrypt

keys = keygen(24)

for a,b in [(1,1), (17,19), (34,62)]:
    ca = encrypt(keys, a)
    cb = encrypt(keys, b)
    a_b = a + b
    ca_cb = (ca + cb) % keys.q
    d_ca_cb = decrypt(keys, ca_cb)

    print(" "*12 + "Expected %d" % a_b)
    print(" "*12 + "Received %d" % d_ca_cb)

    if a_b == d_ca_cb:
        print(" "*12 + "\x1B[32;1mPassed\x1B[0m")
    else:
        print(" "*12 + "\x1B[31;1mFailed\x1B[0m")
    
    ca = encrypt(keys, a)
    cb = encrypt(keys, b)

    a_b = a + a + a + b + b + b
    ca_cb = (ca + ca + ca + cb + cb + cb) % keys.q
    d_ca_cb = decrypt(keys, ca_cb)

    print(" "*12 + "Expected %d" % a_b)
    print(" "*12 + "Received %d" % d_ca_cb)

    if a_b == d_ca_cb:
        print(" "*12 + "\x1B[32;1mPassed\x1B[0m")
    else:
        print(" "*12 + "\x1B[31;1mFailed\x1B[0m")