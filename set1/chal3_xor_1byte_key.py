#!/usr/bin/env python3
ciph = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")


def how_legit(possible: bytes) -> int:
    score = 0
    for c in possible:
        if is_ascii_printable(c):
            score += 1

    return score


def is_ascii_printable(byte: int) -> bool:
    assert byte < 256
    if byte in list(range(32, 127)):
        # print(f"{chr(byte)} is printable")
        return True

    # print(f"{chr(byte)} is not printable")
    return False


for key in range(256):
    possible = bytes([byte ^ key for byte in ciph])
    score = how_legit(possible)
    
    if score == len(possible):
        print(f"Possible plaintext: {possible}")
        print(f"key: {key}")
        print(f"Score: {score}")

        # b"Cooking MC's like a pound of bacon"
