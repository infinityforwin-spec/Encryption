import random
import string

char=' + + '+string.digits + string.ascii_letters + string.punctuation
char=list(char)
key=char.copy()
random.shuffle(key)
phrase= input('phrase')
cipher_phrase=""
for letter in phrase:
    index=char.index(letter)
    cipher_phrase+=key[index]
print(phrase)
print(cipher_phrase)