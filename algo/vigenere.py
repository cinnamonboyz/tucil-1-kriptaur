from util import clean

def vigenere_encrypt(plain_text, key):
    plain_text = clean(plain_text)
    key = clean(key)

    cipher = ""
    for i, plain_char in enumerate(plain_text):
        key_char = key[i%len(key)] 
        cipher += chr(((ord(plain_char) + ord(key_char)) % 26 + ord('A')))
    return cipher

def vigenere_decrypt(cipher_text, key):
    cipher_text = clean(cipher_text)
    key = clean(key)

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