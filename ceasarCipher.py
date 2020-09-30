# the string to be encrypted/decrypted:
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# The encryption/dycrpytion key:
key = -34

# whether the program ecyrpts or decrypts:
mode = 'decrypt' # set to whether 'encypt' or 'decrypt'

# Every possible symbol that can be encypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
'''
def shift_amount(i):
# function to deal with shift
# Will determine the shift, taking into account the length of the alphabet.
# Takes integer - returns integer
    return i%26


def encrypt(text,required_shift):
    out_string = ''
    text = text.lower()
    for char in text:
        if char not in alphabet:
            out_string = out_string + char
        else:    
            alpha_index = alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index +required_shift)]
    return out_string
'''
# store the encrypted/decrypted form of the message
translated = ''

for symbol in message:
        # Only symbols in the SYMBOLS string can be encrypted or decrypted
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            
            # perform encryption/decyption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key
                
            # handle wraparound, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex -= len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex += len(SYMBOLS)
                
            translated += SYMBOLS[translatedIndex]
        else:
            # Append the symbol w/o encrypting/decrypting:
            translated += symbol

# output
print(translated)


