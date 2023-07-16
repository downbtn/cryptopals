#!/usr/bin/env python3
from binascii import unhexlify
import base64

initial = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print(f"initial: {initial}")
plain = unhexlify(initial)
print(f"plain: {str(plain, 'utf-8')}")
ciph = base64.b64encode(plain)
print(f"ciph: {str(ciph, 'utf-8')}")
