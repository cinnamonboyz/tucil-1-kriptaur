def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.replace(' ', '').upper()
    key = key.upper()

    cipher = ""
    for i, plain_char in enumerate(plain_text):
        key_char = key[i%len(key)] # buat nge korespondenin si key sama plaintextnya n jadi bisa berulang
        cipher += chr(((ord(plain_char) + ord(key_char)) % 26 + ord('A'))) # ditambah ord(A) karena buat kalibrasi
    return cipher

def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.replace(' ', '').upper()
    key = key.upper()

    plain = ""
    for i, cipher_char in enumerate(cipher_text):
        key_char = key[i%len(key)]
        plain += chr(((ord(cipher_char) - ord(key_char)) % 26 + ord('A')))
    
    return plain


if __name__ == "__main__":
    cipher = vigenere_encrypt("thisplaintext", "sony")
    print(cipher)
    plain = vigenere_decrypt(cipher, "sony")
    print(plain)
