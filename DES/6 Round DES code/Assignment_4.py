import random
import numpy as np
import math

# import pyfiglet module
import pyfiglet
from os import path


def toBinary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


result = pyfiglet.figlet_format("CS641 - Assignment - DARK ARMY", font="digital")
print(result)

ciphertext = "iogrspjnkjpnihhjjkisnhsptnftfnlo"
print("Given Password: ", ciphertext)
print("Length of ciphertext: ", len(ciphertext))
print("Ciphertext (Binary): ", toBinary(ciphertext))

diff_char = "405c000004000000"

init_perm = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]

inv_init_perm = []
for i in range(1, 65):
    inv_init_perm.append(init_perm.index(i) + 1)


# print(inv_init_perm)

def hex2bin(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)


def bin2hex(bin_string):
    return hex(int(bin_string, 2))[2:].upper()


print("\n")
result = pyfiglet.figlet_format("Step 1: Find Difference from Characteristics", font="digital")
print(result)

char_seq = hex2bin(diff_char)
diff = ''
for i in inv_init_perm:
    diff += char_seq[i - 1]
print("Difference Found: ", diff)
print("Difference Found (HEX): ", bin2hex(diff))

result = pyfiglet.figlet_format("Step 2: Generate Input Pairs", font="digital")
print(result)

if not path.isfile('inputs.txt'):
    print("Run input_gen.cpp for generating 100000 random inputs")

result = pyfiglet.figlet_format("Step 3: Get Output from Server", font="digital")
print(result)

if not path.isfile('game_outputs.log'):
    print("Run run_game.sh for getting ciphertexts for the 100000 random inputs")
else:
    print("Game Output File Exists")

if not path.isfile('output_pairs.txt'):
    import re

    pattern = re.compile("Slowly, a new text starts appearing on the screen. It reads ...")
    flagged = False

    f = open("output_pairs.txt", "w")

    for line in open("game_outputs.log"):
        if flagged:
            flagged = False
            f.write("{}\n".format(line.strip()))
        else:
            for match in re.finditer(pattern, line):
                if match:
                    flagged = True

    f.close()

else:
    print("Output Pairs File Exists")

result = pyfiglet.figlet_format("Step 4: Convert Output to Binary", font="digital")
print(result)

if not path.isfile('outputs.txt'):
    print("Run strToBin.cpp for converting output to Binary")
else:
    print("Output File Exists")

result = pyfiglet.figlet_format("Step 5: Take input's XOR with Characteristics", font="digital")
print(result)

if not path.isfile('input_pairs.txt'):
    print("Run xorify.cpp for getting XOR of all inputs")
else:
    print("Input Pairs File Exists")

result = pyfiglet.figlet_format("Step 6: Run Analysis and Find KEY And Decrypt Password", font="digital")
print(result)

print("Run DES_MASTER_DECRYPTION.cpp for getting the KEY")


