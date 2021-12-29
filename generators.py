import string
import time
import os

def lcLetters():
    for c in string.ascii_lowercase:
        yield c
    

for letter in lcLetters():
    print(letter)
    time.sleep(0.1)
    os.system('clear')