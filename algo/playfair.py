import numpy as np

ABJAD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def create_bujur(key):
    key_2 = ''
    for char in key:
        if char not in key_2 or char == 'J':
            key_2 += char

    for huruf in ABJAD:
        if huruf not in key_2 and huruf != 'J':
            key_2 += huruf

    bujur = np.array(list(key_2)).reshape((5, 5))

    return bujur

def find_idx(bujur, first, second):
    first_v, first_h = np.where(bujur == first)
    second_v, second_h = np.where(bujur == second)

    return first_v[0], first_h[0], second_v[0], second_h[0]

def playfair_encrypt(plain_text: str, key: str):
    key = key.upper().replace(' ', '').replace('J', '')
    bujur = create_bujur(key)
    plain = plain_text.upper().replace(' ', '').replace('J', 'I')

    i = 0
    while i < len(plain):
        if i != len(plain) - 1:
            if plain[i] == plain[i+1]:
                plain = plain[:i+1] + 'X' + plain[i+1:]
        i += 2

    if len(plain) % 2 != 0:
        plain += 'X'

    bigram = [[plain[i], plain[i+1]] for i in range(0, len(plain), 2)]

    for i, (first, second) in enumerate(bigram):
        first_v, first_h, second_v, second_h = find_idx(bujur, first, second)

        if first_v == second_v:
            bigram[i][0] = bujur[first_v, (first_h + 1) % 5]
            bigram[i][1] = bujur[second_v, (second_h + 1) % 5]
        elif first_h == second_h:
            bigram[i][0] = bujur[(first_v + 1) % 5, first_h]
            bigram[i][1] = bujur[(second_v + 1) % 5, second_h]
        else:
            bigram[i][0] = bujur[first_v, second_h]
            bigram[i][1] = bujur[second_v, first_h]

    return ' '.join(''.join(gram) for gram in bigram)

def playfair_decrypt(cipher_text: str, key: str):
    key = key.upper().replace(' ', '').replace('J', '')
    bujur = create_bujur(key)
    cipher = cipher_text.upper().replace(' ', '')

    bigram = [[cipher[i], cipher[i+1]] for i in range(0, len(cipher), 2)]
    for i, (first, second) in enumerate(bigram):
        first_v, first_h, second_v, second_h = find_idx(bujur, first, second)

        if first_v == second_v:
            bigram[i][0] = bujur[first_v, (first_h - 1) % 5]
            bigram[i][1] = bujur[second_v, (second_h - 1) % 5]
        elif first_h == second_h:
            bigram[i][0] = bujur[(first_v - 1) % 5, first_h]
            bigram[i][1] = bujur[(second_v - 1) % 5, second_h]
        else:
            bigram[i][0] = bujur[first_v, second_h]
            bigram[i][1] = bujur[second_v, first_h]

    return (''.join(''.join(gram) for gram in bigram)).replace('X', '')


if __name__ == "__main__":
    cipher = playfair_encrypt("temui ibu nanti malam", "JALAN GANESHA SEPULUH")
    print(cipher)

    plain = playfair_decrypt(cipher, "JALAN GANESHA SEPULUH")
    print(plain)