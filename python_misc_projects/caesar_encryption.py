import string

# plain_text = "axeeh phkew"
# ====shifting lowercase only=======
# shift =7 
# # shift = 
# # shift  %= 26

# alphabet = string.ascii_lowercase
# shifted = alphabet[shift:] + alphabet[:shift]

# table = str.maketrans(alphabet,shifted)

# encrupted = plain_text.translate(table)

# print(encrupted)

# =========shifting both lowercase, uppercase and special chars=======

def caesar(text,shift,alphabets):
    def shift_alpha(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    
    shifted_alphabet = tuple(map(shift_alpha,alphabets))
    final_alpha = " ".join(alphabets)
    final_shifted_alphabet = ' '.join(shifted_alphabet)
    table = str.maketrans(final_alpha,final_shifted_alphabet)
    return text.translate(table)

plain_text = "this if WORKIN!!"
print(caesar(plain_text,7,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))