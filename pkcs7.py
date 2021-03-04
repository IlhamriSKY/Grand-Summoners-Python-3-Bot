import binascii
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

class PKCS7Encoder(object):
    def __init__(self, k=16):
        self.k = k

    def decode(self, text):
        '''
        Remove the PKCS#7 padding from a text string
        '''
        nl = len(text)
        val = int(binascii.hexlify(text[-1].encode("ascii")), 16)
        #if val > self.k:
        #    raise ValueError('Input is not padded or padding is corrupt')

        l = nl - val
        return text[:l]

    def encode(self, text):
        '''
        Pad an input string according to PKCS#7
        '''
        l = len(text)
        output = StringIO()
        val = self.k - (l % self.k)
        for _ in range(val):
            output.write('%02x' % val)
        return bytes(text, 'utf-8') + binascii.unhexlify(output.getvalue())
