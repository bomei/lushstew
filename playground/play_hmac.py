import hashlib, hmac
import arrow
import time


def genCode(password, nonce):
    raw = str(nonce)
    hex = hmac.new(password.encode(), raw.encode(), hashlib.sha1).hexdigest()
    start = int(hex[-1], 16)
    big_int = int(hex[start:start + 8], 16)
    code = big_int % 1000000
    return code


print(genCode('7DDWRSLGSA45RMGK7NMJSZI4CAPVQDYU', arrow.now().timestamp // 30))

while 1:
    print(genCode('7DDWRSLGSA45RMGK7NMJSZI4CAPVQDYU', arrow.now().timestamp // 30))
    time.sleep(1)
