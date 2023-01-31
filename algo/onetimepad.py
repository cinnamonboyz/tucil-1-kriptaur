import string
import random

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

if __name__ == "__main__":
    otpkey = generate_random_key(100000)
    save_key(otpkey, 'otp_key.txt')

    plainteks = input("Masukkan plainteks: ").upper()
    key = read_key('otp_key.txt')
    ciphertext = encrypt_otp(plainteks, key)
    print("Hasil enkripsi: " + ciphertext)
    
    ciphertext = input("Masukkan ciphertext: ").upper()
    key = read_key('otp_key.txt')
    plainteks = decrypt_otp(ciphertext, key)
    print("Hasil dekripsi: " + plainteks)