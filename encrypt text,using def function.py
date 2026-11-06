def caesar(text,shift,encrypt=True):
    if not encrypt:
        shift=-shift
    alphabet='abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet=alphabet[shift:]+alphabet[:shift]
    translation_table=str.maketrans(alphabet+alphabet.upper(),shifted_alphabet+shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text,shift):
    return caesar(text,shift,True)
def decrypt(text,shift):
    return caesar(text,shift,False)

encrypted_text="courage is found in unlikely places"
print(encrypted_text)
decrypted_text=encrypt(encrypted_text,13)
print(decrypted_text)