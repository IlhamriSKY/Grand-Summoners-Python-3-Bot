# -*- coding: utf-8 -*-
import binascii
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

getapiversion = "anjO9AupBu74vdORIFevgOfmwVvai/puDBqLHx6qLozE0j05m/V9ztNJXC4f7I2yhEH2f7gLWI71tH7gUqnW0G3PMTJc6dD85PhZPfBdYK8Vhp6nBjdyFBkBFwRROyoRUbV3Hy3xVPMRwvQ7n/CC454Y4VhMNX67HZOyiKcYfmQFUVAskp0h4lSDQYyQ1IwtG6aY+opI2HnqbUMpsWy/rTJLsFOp+9mOxTNA8i5+Ue2OUP0NhZFua1Q93yur4FME8rLIV60y93we3bkoUMuuwg=="

k = 16
nl = len(getapiversion)
bin_val = bin(int(binascii.hexlify(getapiversion[-1].encode("ascii")), 16))
val = int(binascii.hexlify(getapiversion[-1].encode("ascii")), 16)

#if val > k:
#    raise ValueError('Input is not padded or padding is corrupt')


l = nl - val
print ('DATA')
print (nl)
print (val)
#print (bin_val)
print ('RETURN')
print(l)
print(len(getapiversion[:l]))
print(getapiversion[:l])
