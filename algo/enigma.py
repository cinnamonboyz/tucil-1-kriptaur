from collections import deque
import string

LETTERS = string.ascii_uppercase

def enigma(text, key):
    rotor_1 = deque('BDFHJLCPRTXVZNYEIWGAKMUSQO')
    rotor_2 = deque('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    rotor_3 = deque('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

    rotor_1.rotate(-rotor_1.index(key[0]))
    rotor_2.rotate(-rotor_2.index(key[1]))
    rotor_3.rotate(-rotor_3.index(key[2]))
    # print(deque(LETTERS), rotor_1, rotor_2, rotor_3, deque(reflector), sep='\n')

    result = ""
    for i, char in enumerate(text.upper().replace(' ', '')):
        char = rotor_1[LETTERS.index(char)]
        char = rotor_2[LETTERS.index(char)]
        char = rotor_3[LETTERS.index(char)]
        char = reflector[LETTERS.index(char)]
        char = LETTERS[rotor_3.index(char)]
        char = LETTERS[rotor_2.index(char)]
        char = LETTERS[rotor_1.index(char)]

        rotor_1.rotate(-1)
        if i % 26:
            rotor_2.rotate(-1)
        if i % 26 ** 2:
            rotor_3.rotate(-1)

        result += char

    return result

if __name__ == '__main__':
    plain_text = "malam ini saya gabut malam ini saya gabut malam ini saya gabut malam ini saya gabut "
    cipher = enigma(plain_text, 'AAA')
    print(cipher)

    plain = enigma(cipher, 'AAA')
    print(plain)

