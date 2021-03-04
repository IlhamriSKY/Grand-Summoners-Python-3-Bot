# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import json

import binascii

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

key='ZFlyUU0ycFJaTVlFRkVoaA=='

k = 16

data = "anjO9AupBu74vdORIFevgOfmwVvai/puDBqLHx6qLozE0j05m/V9ztNJXC4f7I2yhEH2f7gLWI71tH7gUqnW0G3PMTJc6dD85PhZPfBdYK8Vhp6nBjdyFBkBFwRROyoRUbV3Hy3xVPMRwvQ7n/CC454Y4VhMNX67HZOyiKcYfmQFUVAskp0h4lSDQYyQ1IwtG6aY+opI2HnqbUMpsWy/rTJLsFOp+9mOxTNA8i5+Ue2OUP0NhZFua1Q93yur4FME8rLIV60y93we3bkoUMuuwg=="
login = "SeUvfQZbG0V6fpgFCWVsp8zvyj/jG0kp3GLAWRJmYJHy1rIws+Vpo961wXrxUMNp09Cthw0K/W0/9LL29iT5ba7WUsqfbSYyeLSrFLE80tjEFtG1qiNBRjy4yJwO/IXSLv+6rKQpQOR8ghFVtpGPktk+y854c5ZWNjeRaWL/DV+4UEkk2sV44c/kD4miRYOcOS2qX60ALyl9VLlgUGCepMCT05tCJ4Rw2094mFcMnvP2rTD1hidEGu9a4cjDclIiGy5ux+NSGS/ZhQnPdhDICkvFXIx0FvJ9MzFEyQ7NC6XT+Ug/6rOuBQufcYbWLKln44EXbJgn8oqEQvM0Y6tvsiNEHATNai0A/nrzMAL2/YGC3i4nxdquDSZDV1+wzGWJqP3OYDPgn0yYo2nfzQoyUODL9e341iUtH3/4mcukw+wUxzBYCwSx04MQL2dplLAn5sEnBl6IPvWA6FILVPu1flqWq9n8Y6fTbvi8WJv8iufqusy4sAnTxY1uOCkZ4Gesd3NbL9TUsSaKUXIiCpHPcPNm3AV+TKvQwqbb/hlaYV1fi1IHCuf8V9X/lqFyU8Qt4c3R/2eRLByE5JsTorzu7ruYfDUDrUtXfI367B9pyOoIpJDvYJUJ5aZFOzJji8yPUzaORo6IRiTNaDSSahYw0bBqUFYDR8i75z+Qt54kEew="
login_en = '{"encryption_key": "7CBgsFDlCPqPI2WJ", "session_id": "84huDpfYHk1", "result": {"scenario_master_size": 19193715, "master_version": 404, "master_update_text": "You will need to download\napproximately {0} data.\nIf the data amount is large\nWi-Fi environment is recommended for\ndownloading data.\nDownload will start\nonce you tap OK.", "scenario_master_version": 120, "resource_path": "https://dlkrtysgey8gg.cloudfront.net/resource/dlc_1576464721/", "master_size": 15309504, "resource_version": 183}}'


#a = AES.new(base64.b64decode(key), AES.MODE_CBC, bytes('\x00'*16, 'utf-8')).decrypt(base64.b64decode(login)).decode('utf-8')

padded_data = json.dumps(login_en)
#print(padded_data)
raw_b = AES.new(base64.b64decode(key), AES.MODE_CBC, bytes('\x00'*16, 'utf-8')).encrypt(base64.b64decode(padded_data))
#print(raw_b)
b = base64.b64encode(raw_b)
#print(b)

#DECODE
#nl = len(a)
#val = int(binascii.hexlify(a[-1].encode("ascii")), 16)
#l = nl - val
#print(a[:l])

#ENCODE
l = len(b)
output = StringIO()
val = k - (l % k)
for _ in range(val):
    output.write('%02x' % val)
z = b + binascii.unhexlify(output.getvalue())
print(z)
