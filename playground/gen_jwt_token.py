import jwt

pub = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDvWEO0amFTUXJdF6TsevXNfxEg
is9YfaRzAVef9Dm3CeJKdXqS/KCP1/8iw2tcRWGEY1MiCwp3cegwujWnDr869cCh
FccrhRcWEVwCPEioosvMTajJSgn0nGGZf6HC/qDMT1ESiD0VlWa1miF457mXXbS0
/jKAYJBiCAKU8g+OZQIDAQAB
-----END PUBLIC KEY-----
"""

pri = """
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDvWEO0amFTUXJdF6TsevXNfxEgis9YfaRzAVef9Dm3CeJKdXqS
/KCP1/8iw2tcRWGEY1MiCwp3cegwujWnDr869cChFccrhRcWEVwCPEioosvMTajJ
Sgn0nGGZf6HC/qDMT1ESiD0VlWa1miF457mXXbS0/jKAYJBiCAKU8g+OZQIDAQAB
AoGAdAS9DP9kHhck8Ks9bsRL0kj97GBdEfAVfwnvh8HDGE7aOm2n9QgwbImvSxKf
QCMBmkLrUV04vZ2hh707tLcZSnM/ulOkLGsytPruM5h9cnV3lhsNLt4jtuSlDvVz
j9Z4mxXOVidjNq41Pg4qKDQS8q/vB+x7DtEn/4zvBotr1QECQQD8aswh5yn9RDao
rMiNmHmh2ldSarbJcZFzsQoX9CK3el+oo7XRguBglwRFHDBNIAh92fUiX4KATZRF
QrIzQnhJAkEA8r33Wd/gZj5GH+AJ/K9zYU4yXYdbMdwaHU/D/XrpfxqtxqQ9h6e4
pNLyOStEnwXPD4voL92aLOwW5Dg34xO9PQJBAKphOEsGK0yeV7rBblpNeoSqydiC
2cDd3M1XyjVjAHAStTEy2A6EpgnsxeAUZ/IXVkQE9Ddwerk6JIQfwgNhsakCQAT5
bZsy4kdWGVvH3IyID+Y7kv6lqnHAH+zf2JVWMni/VDZQ4U3pWvhNtlcDkvlrRg38
gPqSIPmwsNtmZ4bIvcUCQQDRybMD4BRDiZm8JG/gKwHwolUUCKtxjljwUiAq6J+A
t/7kQ94wZnOQDADVbcHs9vU/YRvBHUxF9Uky/Gs+Uzm9
-----END RSA PRIVATE KEY-----
"""

payload = {
    'path': ['bee', 'yes', 'example.com', 'aiohttp', 'jenkins'],
}

token = jwt.encode(payload, pri, algorithm='RS256')

print(token.decode())

# token2 = jwt.encode(payload, 'jack-secret')
#
# print(token2.decode())
