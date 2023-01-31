from collections import deque
import string

LETTERS = string.ascii_uppercase
rotor_1 = deque('BDFHJLCPRTXVZNYEIWGAKMUSQO')
rotor_2 = deque('AJDKSIRUXBLHWTMCQGZNPYFVOE')
rotor_3 = deque('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

plain_text = "Galo semuanya"
key = "BAE"

rotor_1.rotate(-rotor_1.index(key[0]))
rotor_2.rotate(-rotor_2.index(key[1]))
rotor_3.rotate(-rotor_3.index(key[2]))
print(deque(LETTERS), rotor_1, rotor_2, rotor_3, deque(reflect), sep='\n')

for char in plain_text.upper():
    char = rotor_1[LETTERS.index(char)]
    print(char)
    break

