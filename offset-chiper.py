"""
Decode and Encode text by changing each char by the given offset
Created by: regi18
Version: 1.0.4
Github: https://github.com/regi18/offset-chiper
"""

import os
from time import sleep

while True:
    # reset variables
    plaintext = ""

    answer = input("\nDecode(d), Encode(e) or Quit(q)? ").upper()
    print("\n")

    # Change every char into his decimal value, add (or subtract) the offset and than save it in plain text.
    try:
        if answer == "D":
            offset = int(input("Enter the offset: "))
            text = input("Enter the text to decode: ")
            for i in text:
                plaintext += chr((ord(i) - offset))
        elif answer == "E":
            offset = int(input("Enter the offset: "))
            text = input("Enter the text to encode: ")
            for i in text:
                plaintext += chr((ord(i) + offset))
        elif answer == "Q":
            break
        else:
            raise ValueError
    except ValueError:  # handle errors
        print("\nError, the entered value is not correct\n")
        sleep(1.2)
        os.system('cls')
        continue

    print("The text is: {}".format(plaintext))
    print("")
    os.system("pause")
    os.system('cls')
