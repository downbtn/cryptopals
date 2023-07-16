#!/usr/bin/env python3
from binascii import hexlify, unhexlify


def xorbuf(buf1: bytes, buf2: bytes) -> bytes:
    assert len(buf1) == len(buf2) # no clue how to handle other cases ngl
    output = []
    for i in range(len(buf1)):
        output.append(buf1[i] ^ buf2[i])
    return bytes(output)


if __name__ == "__main__":
    buf1 = unhexlify("1c0111001f010100061a024b53535009181c")
    buf2 = unhexlify("686974207468652062756c6c277320657965")
    expected = unhexlify("746865206b696420646f6e277420706c6179")

    print(f"calculated result: {str(hexlify(xorbuf(buf1, buf2)), 'utf-8')}")
    print(f"  expected result: {str(hexlify(expected), 'utf-8')}")
