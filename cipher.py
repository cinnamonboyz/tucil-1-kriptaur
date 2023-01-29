print("Selamat datang di program konversi teks Kriptografi!")
print("Silakan pilih program yang ingin dijalankan")
print("1. Vigenere Cipher standard")
print("2. Extended Vigenere Cipher")
print("3. Playfair Cipher")
print("4. One-time pad")

# vigenere cipher
def chartonum(input):
    output = []
    for character in input:
        if character.isalpha():
            uppercase = character.upper()
            num = ord(uppercase) - 65
            output.append(num)
        else:
            continue
    return output

def numtochar(input):
    output = []
    for number in input:
        num = number + 65
        character = chr(num)
        output.append(character)
    return output

def encrypt_vigenere(plainteks, key):
    p = chartonum(plainteks)
    k = chartonum(key)
    ciphertext = []
    for i in range(len(p)):
        num = (p[i] + k[i % len(k)]) % 26
        ciphertext.append(num)
    ciphertext = numtochar(ciphertext)
    return ''.join(ciphertext)

def decrypt_vigenere(ciphertext, key):
    c = chartonum(ciphertext)
    k = chartonum(key)
    plainteks = []
    for i in range(len(c)):
        num = (c[i] - k[i % len(k)]) % 26
        plainteks.append(num)
    plainteks = numtochar(plainteks)
    return ''.join(plainteks)

# extended vigenere cipher
def chartonum_ascii(input):
    output = []
    for character in input:
        num = ord(character)
        output.append(num)
    return output

def numtochar_ascii(input):
    output = []
    for number in input:
        character = chr(number)
        output.append(character)
    return output

def encrypt_extended_vigenere(plainteks, key):
    p = chartonum_ascii(plainteks)
    k = chartonum_ascii(key)
    ciphertext = []
    for i in range(len(p)):
        num = (p[i] + k[i % len(k)]) % 256
        ciphertext.append(num)
    ciphertext = numtochar_ascii(ciphertext)
    return ''.join(ciphertext)

def decrypt_extended_vigenere(ciphertext, key):
    c = chartonum_ascii(ciphertext)
    k = chartonum_ascii(key)
    plainteks = []
    for i in range(len(c)):
        num = (c[i] - k[i % len(k)]) % 256
        plainteks.append(num)
    plainteks = numtochar_ascii(plainteks)
    return ''.join(plainteks)

# one-time pad
import string
import random

def generate_random_key(length):
    key = [random.choice(string.ascii_uppercase) for i in range(length)]
    return ''.join(key)

def save_key(key, filename):
    with open(filename, 'w') as f:
        f.write(key)

def read_key(filename):
    with open(filename, 'r') as f:
        key = f.read()
    return key

def encrypt_otp(plainteks, key):
    p = chartonum(plainteks)
    k = chartonum(key)
    ciphertext = []
    for i in range(len(p)):
        num = (p[i] + k[i]) % 26
        ciphertext.append(num)
    ciphertext = numtochar(ciphertext)
    return ''.join(ciphertext)

def decrypt_otp(ciphertext, key):
    c = chartonum(ciphertext)
    k = chartonum(key)
    plainteks = []
    for i in range(len(c)):
        num = (c[i] - k[i]) % 26
        plainteks.append(num)
    plainteks = numtochar(plainteks)
    return ''.join(plainteks)

# main program
program = input("Pilih program: ")
if program == "1":
    print("Anda memilih Vigenere Cipher standard")
    print("Silakan pilih mode yang ingin dijalankan")
    print("1. Enkripsi")
    print("2. Dekripsi")
    mode = input("Pilih mode: ")
    
    if mode == "1":
        plainteks = input("Masukkan plainteks: ").upper()
        key = input("Masukkan kunci: ").upper()
        ciphertext = encrypt_vigenere(plainteks, key)
        print("Hasil enkripsi: " + ciphertext)
    
    if mode == "2":
        ciphertext = input("Masukkan ciphertext: ").upper()
        key = input("Masukkan kunci: ").upper()
        plainteks = decrypt_vigenere(ciphertext, key)
        print("Hasil dekripsi: " + plainteks)

if program == "2":
    print("Anda memilih Extended Vigenere Cipher")
    print("Silakan pilih mode yang ingin dijalankan")
    print("1. Enkripsi")
    print("2. Dekripsi")
    mode = input("Pilih mode: ")
    
    if mode == "1":
        plainteks = input("Masukkan plainteks: ")
        key = input("Masukkan kunci: ")
        ciphertext = encrypt_extended_vigenere(plainteks, key)
        print("Hasil enkripsi: " + ciphertext)
    
    if mode == "2":
        ciphertext = input("Masukkan ciphertext: ")
        key = input("Masukkan kunci: ")
        plainteks = decrypt_extended_vigenere(ciphertext, key)
        print("Hasil dekripsi: " + plainteks)

if program == "3":
    print("Anda memilih Playfair Cipher")
    print("Silakan pilih mode yang ingin dijalankan")
    print("1. Enkripsi")
    print("2. Dekripsi")
    mode = input("Pilih mode: ")
    
    if mode == "1":
        plainteks = input("Masukkan plainteks: ").upper()
        key = input("Masukkan kunci: ").upper()
        ## ciphertext = encrypt_playfair(plainteks, key)
        print("Hasil enkripsi: " + ciphertext)
    
    if mode == "2":
        ciphertext = input("Masukkan ciphertext: ").upper()
        key = input("Masukkan kunci: ").upper()
        ## plainteks = decrypt_playfair(ciphertext, key)
        print("Hasil dekripsi: " + plainteks)

if program == "4":
    print("Anda memilih One-time pad")
    print("Silakan pilih mode yang ingin dijalankan")
    print("1. Enkripsi")
    print("2. Dekripsi")
    mode = input("Pilih mode: ")

    # generate randome one time pad key
    otpkey = generate_random_key(100000)
    save_key(otpkey, 'otp_key.txt')

    if mode == "1":
        plainteks = input("Masukkan plainteks: ").upper()
        key = read_key('otp_key.txt')
        ciphertext = encrypt_otp(plainteks, key)
        print("Hasil enkripsi: " + ciphertext)
    
    if mode == "2":
        ciphertext = input("Masukkan ciphertext: ").upper()
        key = read_key('otp_key.txt')
        plainteks = decrypt_otp(ciphertext, key)
        print("Hasil dekripsi: " + plainteks)