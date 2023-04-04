def cipher(plaintext: str, alphabet: str, shift: int = 1):
    plaintext = plaintext.upper()
    ciphertext = ""
    other = ""
    for c in plaintext:
        if not c.isalpha():
            other += c
            continue
        index = alphabet.index(c)
        if index + shift < (len(alphabet) - 1):
            ciphertext += alphabet[index + shift]
        else:
            ciphertext += alphabet[index + shift - (len(alphabet) - 1) - 1]
    ciphertext += other
    return ciphertext
